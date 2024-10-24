# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-sigprofilermatrixgenerator
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilermatrixgenerator
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilermatrixgenerator(PythonPackage):
    """SigProfilerMatrixGenerator creates mutational matrices for all types of somatic mutations. It allows downsizing the generated mutations only to parts of the genome (e.g., exome or a custom BED file). The tool seamlessly integrates with other SigProfiler tools."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerMatrixGenerator"

    url = "https://github.com/AlexandrovLab/SigProfilerMatrixGenerator/archive/refs/tags/v1.2.30.tar.gz"

    license("BSD 2-Clause")

    version(
        "1.2.30",
        sha256="ab8054d861831ff8e318082adac51b8015df51d820a335132271fa2801ac70ab",
    )
    version(
        "1.2.29",
        sha256="c79df0ed2436aa4df93cd0ba26fd783fcc269815986536606ecd14e7ff735822",
    )
    version(
        "1.2.28",
        sha256="420edc2cfe26ea9da90974d507a44c1ecff7824ef9410c9bcf24d33561b6dc1a",
    )
    version(
        "1.2.27",
        sha256="04a698409a11c26c59e28953f58dad08c15566345f5ebcc93b52767f918ee10a",
    )
    version(
        "1.2.26",
        sha256="b179e50f7c509e626ee8191f54274737c93e9f3487d3159825a9713d1b6d4c21",
    )
    version(
        "1.2.25",
        sha256="a1be9ae835e693c54107f7a10c446e8d18d2c8b7601bd65dfc79a17551c267d2",
    )
    version(
        "1.2.24",
        sha256="bb2c9267b561f35f5e7b6a6743d40a9968c7e6c4761a3648539a91ab252d86e1",
    )
    version(
        "1.2.23",
        sha256="0c6d4d0f18f373028ceb3e4572d0cb0930d0308ec53b2bd6bc0d714827fbc5bd",
    )
    version(
        "1.2.22",
        sha256="61e8df7e4327753dabc6b38b581bf4fa297c1ad1eba9efd421b8e5243585c00a",
    )
    version(
        "1.2.21",
        sha256="b25a7959f6f93a8b76e211d490de4d642c8e7f5a0089a421eda383ef5920ec4e",
    )

    depends_on("python@3.8:3.11", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-sigprofilerplotting", type=("build", "run"))
