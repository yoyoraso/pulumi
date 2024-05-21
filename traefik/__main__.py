import pulumi

from pulumi_kubernetes.helm.v3 import Release, ReleaseArgs, RepositoryOptsArgs
from pulumi_kubernetes.yaml import ConfigFile
from pulumi_kubernetes import Provider
from pulumi_command import local

import subprocess

traefik = Release(
    "traefik-ikube",
    ReleaseArgs(
        name="traefik",
        chart="traefik",
        version="28.0.0",
        create_namespace=True,    
        namespace="traefik",
        value_yaml_files=[pulumi.FileAsset("./values.yaml")],
        repository_opts=RepositoryOptsArgs(
            repo="https://traefik.github.io/charts",
        ),
    ),
)


pulumi.export("name", traefik.name)
