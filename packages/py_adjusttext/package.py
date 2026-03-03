0# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdjusttext(PythonPackage):
    """Automatic label placement for matplotlib."""

    homepage = "https://github.com/Phlya/adjustText"
    pypi = "adjustText/adjustText-0.8.tar.gz"

    version("0.8", sha256="bb0682bb53abb626d6afc9c1db108ccb67f2c35ddc8d20ac6a802c756c07ee17")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-bioframe", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
