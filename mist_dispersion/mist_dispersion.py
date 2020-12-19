from lina import lina
import argparse
import os

def reverse(dispersed_dir, output_file, original_size):
    filenames = os.listdir(dispersed_dir)
    filenames.sort()
    dispersed_data_list = []
    for filename in filenames:
        f = open(dispersed_dir + "/" + filename, "rb")
        dispersed_data_list.append("".join(lina.message_to_binary(f.read())))
        f.close()
    i = 0
    result = ""
    while True:
        j = i % len(filenames)
        k = i // len(filenames)
        if i / 8 > original_size:
            break
        result += dispersed_data_list[j][k]
        i += 1
    f = open(output_file, "wb")
    f.write(lina.split(result))
    f.close()

def disperse(filepath, output_dir):
    output_file_length = 8
    if output_dir is None:
        output_dir = "./output"
        os.mkdir(output_dir)
    f = open(filepath, "rb")
    binary = "".join(lina.message_to_binary(f.read()))
    f.close()
    results = []
    for i in range(output_file_length):
        results.append("")
    for b in range(len(binary)):
        bit = binary[b]
        bi = b % output_file_length
        results[bi] += bit
    for i in range(len(results)):
        results[i] += "0" * (8 - (len(results[i]) % 8))
    for i in range(output_file_length):
        results[i] = lina.split(results[i])
        f = open(output_dir + "/data-" + str(i).zfill(8), "wb")
        f.write(results[i])
        f.close()



def main():
    parser = argparse.ArgumentParser(description="mist-dispersion is a file disperser")
    parser.add_argument("mode", help="disperse or reverse")
    parser.add_argument("-f", "--file")
    parser.add_argument("-d", "--dir")
    parser.add_argument("-o", "--output")
    parser.add_argument("-s", "--size")
    args = parser.parse_args()
    d = args.dir
    if args.mode == "disperse":
        disperse(args.file, d)
    elif args.mode == "reverse":
        if args.output is None or args.size == None:
            parser.print_help()
        else:
            reverse(d, args.output, int(args.size))

if __name__ == "__main__":
    main()
