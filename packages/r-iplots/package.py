# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIplots(RPackage):
    """iPlots - Interactive Graphics for R

    Interactive plots for R.
    """

    homepage = "http://www.iPlots.org/"
    cran = "iplots"

    version("1.1-8", md5="fc5a76df91251eaa4e4f4dd09008cf9c")

    depends_on("r@1.5:", type=("build", "run"))
    depends_on("r-rjava@0.5.0:", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("libxtst", type=("build", "run", "link"))
    depends_on("libxi", type=("build", "run", "link"))

    def setup_build_environment(self, env):
        env.set("NOAWT", "1")
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libxtst"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libxi"].prefix.lib)
