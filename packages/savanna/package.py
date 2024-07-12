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
    url = "https://github.com/CODARcode/savanna/archive/refs/tags/v0.5.tar.gz"

    version("0.5", sha256="ffc352a2328eb3d3e35851a2df364bd486d66dd780673a2d803ab1f9ba3f7161")

    resource(name="HeatTransfer", url="https://github.com/CODARcode/Example-Heat_Transfer/archive/3f037ddae896e6c3dc44793114910e970f0d2e05.tar.gz", sha256="d2340fe4f2ba27d079918ce2676efb62776ef436577b91cac1deb4799217f83a", destination="Heat_Transfer")

    variant("tau", default=False, description="Enable TAU profiling support")

    depends_on("mpi")
    depends_on("stc")
    depends_on("adios +fortran +zlib +sz +zfp staging=dataspaces")  # flexpath
    depends_on("turbine")
    depends_on("tau", when="+tau")

    def install(self, spec, prefix):
        install_tree(".", prefix)
