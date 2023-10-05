# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAwsEc2metadata(RPackage):
    """Retrieve Amazon EC2 instance metadata from within the running instance."""

    homepage = "https://github.com/cloudyr/aws.ec2metadata"
    cran = "aws.ec2metadata"

    version("0.2.0", sha256="08895e2a47a63ef5de0eef6ee6c19600f17c039bf9d645390cd08febc49374d1")
    version("0.1.6", sha256="f647930d9b5eb0db3b277894a96cd11bc3f0d5fc1a100d6a2a51b069fe7c9955")
    version("0.1.5", sha256="3bd0cc28c266ecbc5b3463546750c5a44ff7a35aaba90de73ec30b2f9bb8fb1c")
    version("0.1.4", sha256="5cab4cedb64b924479f55ca3812dff6b952b85af6107016736ce5061b17d8122")
    version("0.1.2", sha256="b49614b740140fcc12c85e6e1fd6471416841cfe23df06cded96c943478e9df9")
    version("0.1.1", sha256="39a36a5f41a58c9c8c63d207a60b29a72d1e66ca6549e8635016fe9df7a7f177")

    depends_on("r-curl", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
