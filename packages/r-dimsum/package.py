# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimsum(RPackage):
    """An error model and pipeline for analyzing deep mutational scanning (DMS) data and diagnosing common experimental pathologies."""

    homepage = "https://github.com/lehner-lab/DiMSum"
    url = "https://github.com/lehner-lab/DiMSum/archive/refs/tags/v1.3.tar.gz"

    version("1.3", sha256="5f4181a8f4790f7a995db3f1d19408ebeb0fe00ed0cf520d28b1e37dc53a01ea")
    version("1.2.11", sha256="46527d28b4740eda76cac037f4f4442108767c24a1025a4c4bb4e30b5d78e86d")
    version("1.2.10", sha256="4951f2c5e99b24591b5f51169b1cec3ecfdedab9ad597c9e6adb4248c5ea5900")
    version("1.2.9", sha256="2689b81ec053fd599961d354c39eaf135da4b54cc0ff5d56b82801f4e6f5c167")
    version("1.2.8", sha256="615197da093caf08a4d2348f83d9438c12cd82c9e1a09e686b5279bbeaa05d23")
    version("1.2.7", sha256="fe6385f5b58ef1bb8692c3e5c369dd76482bd4ac35f5044c611ade7c409512e1")
    version("1.2.5", sha256="15997e8e6273fc542a06669cf20365604ba6be015fcf8fa59375c50e1a546197")
    version("1.2.0", sha256="c02d2e8c68601205f17c0fbe11d38f8005cdb6a36240faf7b32e03b0b8470e88")
    version("1.1.4", sha256="a677a383ac1f09abf6e39bb5d5591fa4e474e93db3c46adb1124d6948c053081")
    version("1.1.3", sha256="df31db07947a1616ca81ffe566d59ad68daf49a9e355ec1c113e7107c131b8ca")

    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-cairo", type=("build", "run"))
    depends_on("r-ggally", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-shortread", type=("build", "run"))
