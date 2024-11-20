import subprocess

def generate(name, username, stats):
    print(stats)
    template_file = open("template.typ",'r')
    template = template_file.read()
    template = template.format(name, username, *list(map(lambda x: float("{:.2f}".format(x * 100)), stats[0:5])))
    template_file.close()
    
    report_file = open(f"PDF/{username}.typ",'w+')
    report_file.write(template)
    report_file.close()
    print(f"Generating report for {username}...")

    subprocess.call(["typst", "compile", f"PDF/{username}.typ", f"PDF/{username}.pdf"])