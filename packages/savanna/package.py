# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Savanna(MakefilePackage):
    """CODARcode Savanna runtime framework for high performance,
    workflow management using Swift/T and ADIOS.
    """

    homepage = "https://github.com/CODARcode/savanna"
    git = "https://github.com/CODARcode/savanna.git"

    version("0.5", tag="v0.5", submodules=True)

    variant("tau", default=False, description="Enable TAU profiling support")

    depends_on("mpi")
    depends_on("stc")
    depends_on("adios +fortran +zlib +sz +zfp staging=dataspaces")  # flexpath
    depends_on("turbine")
    depends_on("tau", when="+tau")

    def install(self, spec, prefix):
        install_tree(".", prefix)
