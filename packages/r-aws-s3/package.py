# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAwsS3(RPackage):
    """A simple client package for the Amazon Web Services ('AWS') Simple Storage Service ('S3') 'REST' 'API' <https://aws.amazon.com/s3/>.."""

    homepage = "https://github.com/cloudyr/aws.s3"
    cran = "aws.s3"

    version("0.3.21", sha256="bd21054ab63555d294e7465dcb6c86f107db52ba841aeac5bdf4d00af0674c8c")
    version("0.3.20", sha256="6c6d0f6e2aa753bd011b4642524e5cd89a3b36f5f46c564bee098b747c81c40a")
    version("0.3.12.1", sha256="f850391b26456476f59044e94a4da54a267e8e283d0d155939845dfcb02f92db")
    version("0.3.12", sha256="348fbbd976b5bcfbb60024864b5859fa3fce6071d5204667ff158296614cd1f9")
    version("0.3.11", sha256="4cab9bab8b5a88c1d450c4b3aa292224a44a00aa4a03801f40c9a0157b0a627d")
    version("0.3.3", sha256="8393ce41e5097cdc5a798834f8718772432903c3614e9bdad5d1f9e6def464ee")
    version("0.3.1", sha256="8feb32caca5564a99d022d4afeee1d71eb2123c9fc6dbad4c088db04afabf5fc")

    depends_on("r-curl", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-xml2@1.0.0:", type=("build", "run"))
    depends_on("r-base64enc", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-aws-signature", type=("build", "run"))
