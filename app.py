from flask import Flask, render_template, request, jsonify
import hashlib, random, time

app = Flask(__name__)

# USERS
user_db = {
    "admin": "password123",
    "carol": "carol@123",
    "john": "john123",
    "username": "password",
    "alice": "alice@2026"
}

secure_db = {u: hashlib.sha256(p.encode()).hexdigest() for u,p in user_db.items()}

failed_attempts = {}
attack_count = 0
fail_count = 0
logs = []

def add_log(msg):
    logs.append(msg)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs")
def get_logs():
    return jsonify(logs[-30:])

@app.route("/stats")
def stats():
    return jsonify({"attacks": attack_count, "fails": fail_count})

@app.route("/graph")
def graph():
    return jsonify({
        "labels": ["Attacks", "Failures"],
        "values": [attack_count, fail_count]
    })

@app.route("/attack")
def attack():
    global attack_count
    common = ["123456","admin","password","password123"]

    for pwd in common:
        time.sleep(0.15)
        add_log(f"⚡ Trying {pwd}")
        if pwd in user_db.values():
            attack_count += 1
            add_log(f"🔥 Password cracked: {pwd}")
            return jsonify({"status":"cracked"})

    add_log("❌ Attack failed")
    return jsonify({"status":"fail"})

@app.route("/insecure", methods=["POST"])
def insecure():
    global fail_count
    u = request.form.get("username")
    p = request.form.get("password")

    if user_db.get(u) == p:
        add_log(f"✅ Insecure login success: {u}")
        return jsonify({"status":"success"})
    else:
        fail_count += 1
        add_log(f"❌ Insecure login failed: {u}")
        return jsonify({"status":"fail"})

@app.route("/secure", methods=["POST"])
def secure():
    global fail_count
    u = request.form.get("username")
    p = request.form.get("password")

    failed_attempts.setdefault(u, 0)

    if failed_attempts[u] >= 3:
        add_log(f"🚫 {u} locked")
        return jsonify({"status":"locked"})

    hashed = hashlib.sha256(p.encode()).hexdigest()

    if secure_db.get(u) == hashed:
        otp = str(random.randint(1000,9999))
        add_log(f"🔐 Secure login success: {u}")
        return jsonify({"status":"otp","otp":otp})
    else:
        failed_attempts[u] += 1
        fail_count += 1
        add_log(f"❌ Secure login failed: {u}")
        return jsonify({"status":"fail"})

if __name__ == "__main__":
    app.run(debug=True)