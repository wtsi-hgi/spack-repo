# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuppdists(RPackage):
    """Supplemental Distributions

    Functions for random number generation and density evaluation for some
    well-known discrete and continuous distributions that are not in base R.
    """

    homepage = "https://cran.r-project.org/package=SuppDists"
    cran = "SuppDists"

    # Version used by upstream spack at time of writing
    version("1.1-9.7", sha256="6b5527e2635c0ff762eb7af8154704c85e66d7f79a9524089a5c98dfa94dab08")

    # No extra deps beyond what upstream defines; rely on defaults

    def setup_build_environment(self, env):
        # R >= 4.5 triggers a build error in SuppDists where PI is undeclared
        # Ensure PI is defined via compiler flags for this build only
        if self.spec.satisfies("^r@4.5:"):
            define_pi = "-DPI=3.14159265358979323846"
            env.append_flags("PKG_CPPFLAGS", define_pi)
            env.append_flags("PKG_CXXFLAGS", define_pi)
