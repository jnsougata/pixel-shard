import sys
import deta_cli


MICROS = [
    'shard-zero',
    'shard-one',
    'shard-two',
    'shard-three',
    'shard-four',
    'shard-five',
    'shard-six',
    'shard-seven',
    'shard-eight',
    'shard-nine',
]

def main():
    deta_access_key = sys.argv[1]
    if not deta_access_key:
        raise sys.exit('No Deta access key provided')

    client = deta_cli.DetaClient(deta_access_key)

    for name in MICROS:
        try:
            micro = client.get_micro(name)
            micro.remove_deps('aiotube', 'fastapi')
            micro.add_deps('aiotube', 'fastapi')
            micro.deploy(scripts=['main.py', 'requirements.txt'])
            sys.stdout.write(f'[SUCCESS] {name} deployed...')
        except Exception as e:
            sys.stdout.write(f'[ERROR] {name} failed to deploy...')
            sys.stdout.write(e)


if __name__ == '__main__':
    main()
    