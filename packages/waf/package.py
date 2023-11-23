# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Waf(Package):
    """Waf is a Python-based framework for configuring, compiling and installing applications."""

    homepage = "https://waf.io/"
    git = "https://gitlab.com/ita1024/waf/"

    version("2.0.26", branch="waf-2.0.26")

    depends_on("python@2.7:", type=("build", "run"))

    def install(self, spec, prefix):
        which("./waf-light")("--make-waf")

        mkdir(prefix.bin)
        install("waf", prefix.bin.waf)

