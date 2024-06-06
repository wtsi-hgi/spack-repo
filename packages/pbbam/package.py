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
#     spack install pbbam
#
# You can edit this file again by typing:
#
#     spack edit pbbam
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbbam(MesonPackage):
    """
    The pbbam software package provides components to create, query,
    & edit PacBio BAM files and associated indices.
    These components include a core C++ library,
    bindings for additional languages, and command-line utilities.
    """

    homepage = "https://github.com/PacificBiosciences/pbbam"
    url = "https://github.com/PacificBiosciences/pbbam/archive/v2.4.0.tar.gz"

    maintainers("snehring")

    license("PacBio open source license")

    version(
        "2.4.0",
        sha256="a386a5231b06b0ea660d81abe8081041c200d1817710b89bc9888b485a7aab26",
    )

    depends_on("zlib-api", type=("build", "run"))
    depends_on("boost", type=("build", "run"))
    depends_on("cmake", type="build")
    depends_on("htslib@1.7:", type=("build", "run"))
    depends_on("pbcopper", type=("build", "run"))

    def meson_args(self):
        return ["-Dtests=false"]

    # def setup_build_environment(self, env):
    #     env.set("BOOST_ROOT", self.spec["boost"].prefix)

    # def setup_dependent_build_environment(self, env, dependent_spec):
    #     env.set("PacBioBAM_LIBRARIES", self.prefix.lib)
    #     env.set("PacBioBAM_INCLUDE_DIRS", self.prefix.include)
