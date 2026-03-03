# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for
# details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMarsilea(PythonPackage):
    """Declarative creation of composable Matplotlib visualizations."""

    homepage = "https://github.com/Marsilea-viz/marsilea"
    pypi = "marsilea/marsilea-0.5.8.tar.gz"

    license("MIT")

    version("0.5.8", sha256="9066e3004dbc1e980f4c24f37cf796d3cbaf05041eea6487edafb315959efc45")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-uv-dynamic-versioning", type="build")
    depends_on("py-legendkit", type=("build", "run"))
    depends_on("py-matplotlib@3.6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-platformdirs", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import marsilea")
