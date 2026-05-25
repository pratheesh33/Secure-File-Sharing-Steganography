if "stego_image" in request.files:
            img = request.files["stego_image"]

            if not img.filename.lower().endswith(".png"):
                flash("Only PNG stego images allowed")
                return render_template("index.html")

            path = os.path.join(UPLOAD, img.filename)
            img.save(path)
            stego = cv2.imread(path)

            try:
                encrypted, filename = extract_file_from_image(stego)
            except ValueError as e:
                flash(str(e))
                return render_template("index.html")

            original = rc6_decrypt(encrypted, KEY)
            out_file = os.path.join(DECRYPTED, filename)
            open(out_file, "wb").write(original)

            return send_from_directory(DECRYPTED, filename, as_attachment=True)

    return render_template("index.html")
