# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenxlsx(RPackage):
    """Read, Write and Edit xlsx Files.

    Simplifies the creation of Excel .xlsx files by providing a high level
    interface to writing, styling and editing worksheets. No Java required.
    """

    cran = "openxlsx"

    version("4.2.8", sha256="8a0861ab8b677f6cd5f582f7c6721c0451cd04d65c6e9cc6ebdb7fbc6597e4d8")
    version("4.2.7.1", sha256="f12f6293be963505df5c6d9fdc8149bb0b3a7003721b259451ce2e4a4840fbf1")
    version("4.2.7", sha256="5fbec00b2feb8e673ff35872ba292dfac6d18d4808069581baf2b1e27836afce")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-zip", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
