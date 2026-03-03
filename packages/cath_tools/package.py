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
#     spack install cath-tools
#
# You can edit this file again by typing:
#
#     spack edit cath-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class CathTools(CMakePackage):
    """Protein structure comparison tools such as SSAP, as used by the Orengo Group in curating CATH."""

    homepage = "https://github.com/UCLOrengoGroup/cath-tools"
    url = "https://github.com/UCLOrengoGroup/cath-tools/archive/refs/tags/v0.16.10.tar.gz"

    license("GPL-3.0")

    version("0.16.10", sha256="b824998a73b97308e2a19ea41ae1043723444f3887b4a318d161731c2b326884")
    version("0.16.5", sha256="10b2913edf70cda698a47003d4f1ad8de89fc73ccacdafb1d75ce444be25bffe")
    version("0.16.4", sha256="0a6360f05fd5c18eaefd6263efe0f2e6ac8f35e63d05463fbbfbda8cf2a06336")
    version("0.16.2", sha256="8a653137d2b51a907e6a6eca8fbee8b0ef7a6127b0f3687f18d93a2d9853953c")
    version("0.16.0", sha256="f265db9ae73b374eb799c2d4e220d4a418232872b1463f880e3c966d8bc3442b")
    version("0.15.3", sha256="971b1cc0485324c77475596a6942d7f000e79969f6ab3fd5d80a180ea804856a")
    version("0.15.2", sha256="a0c0531e0de894323758c3831a3f4b1d6fe364fb83d14a950763c8ad6dc4e393")
    version("0.15.1", sha256="450a15bbfe1eb61d1248736bb64520a7e17773a953aa46a6cb9b44a6b3a0cad1")
    version("0.14.4", sha256="6bf10872ffa306242eb5aac9fa47bf0d866507d85510b406f53bfad9f023ed16")
    version("0.14.2", sha256="b6299d9d705a194c0c84a219bd7bc3b7cc638f58269052c8f2ea31b489dc83e7")

    depends_on("gsl")
    depends_on("boost@1.60+filesystem+iostreams+log+program_options+serialization+timer+test")

    def patch(self):
        filter_file(
            "#include <boost/format.hpp>",
            """#include <boost/format.hpp>
#include <fstream>""",
            "source/ct_cluster/cath/cluster/map/aggregate_map_results.cpp",
            string=True,
        )
        filter_file(
            "#include <boost/filesystem.hpp>",
            """#include <boost/filesystem.hpp>
#include <limits>""",
            "source/ct_test/cath/test/global_test_constants.hpp",
            string=True,
        )
