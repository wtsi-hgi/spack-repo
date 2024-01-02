# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSpdl(RPackage):
    """Logging functions in 'RcppSpdlog' provide access to the logging functionality from the 'spdlog' 'C++' library."""

    homepage = "https://github.com/eddelbuettel/spdl"
    cran = "spdl"

    version("0.0.5", sha256="2d7a888eec3f582df61ba7a2dcf27cbf886dc3696cdf6e44c04c1da638fdb8a0")
    version("0.0.4", sha256="2002c70b5af577db0b3d731f90b4dd549886d0173b559deb05225c8257ed1ee0")
    version("0.0.3", sha256="08b8d763aa4c68fe475c97a9f01f3fc3d3992dfc7c09f7786f41800430f01509")
    version("0.0.2", sha256="a78da42e40d8a96041f72eedb427defd865134527c835610c7e24526ba0e3ca2")
    version("0.0.1", sha256="59d90562c9fc642cdac9b1477d6cc15465b454b88b543a8a383eaf7bfbf6e98d")

    depends_on("r-rcppspdlog@0.0.13:", type=("build", "run"))
