from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name:
        file_path = f'/tmp/data/{file_name}.txt'

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if line_number:
                    line_number = int(line_number)
                    if 1 <= line_number <= len(lines):
                        return lines[line_number - 1]
                
                # If line_number is not provided or invalid, return the entire content
                return ''.join(lines)
        except FileNotFoundError:
            return ''  # Return an empty string for a nonexistent file
    else:
        return ''  # Return an empty string for an invalid request

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
