import sys
import deta_cli


MICROS = [
    'shard-backup',
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
    
    try:
        client = deta_cli.DetaClient(deta_access_key)
    except Exception as e:
        raise sys.exit(f'Error: Invalid Deta access key...')
    else:
        for name in MICROS:
            sys.stdout.write(f'Deploying to micro: {name}...')
            try:
                micro = client.get_micro(name)
                #micro.add_deps(['xmltodict'])
                micro.deploy(scripts=['main.py', 'requirements.txt', 'utils.py'])
                sys.stdout.write(f'[SUCCESS] {name} deployed...')
            except Exception as e:
                sys.stdout.write(f'[ERROR] {name} failed to deploy...')
                sys.stdout.write(str(e))


if __name__ == '__main__':
    main()
