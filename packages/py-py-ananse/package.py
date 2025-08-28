# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyAnanse(PythonPackage):
    """ANANSE: Prediction of key transcription factors in cell fate
    determination using enhancer networks."""

    homepage = "https://github.com/vanheeringen-lab/ANANSE"
    url = "https://github.com/vanheeringen-lab/ANANSE/archive/refs/tags/v0.5.1.tar.gz"
    list_url = "https://github.com/vanheeringen-lab/ANANSE/releases"

    license("MIT")

    # Releases from GitHub tags
    version("0.5.1", sha256="3ce5a41dbedb83913fdd451692cbf7df0e4ad3bd102d1ce67f9379329b35142b")
    version("0.5.0", sha256="5adc317e5055ecffd2389c63d77639b88cebb952159edb3ab365a4f6bfda9d13")
    version("0.4.1", sha256="4b8c63294c0ddf85247a3394e68756ce928d0d89a6d4b3e613dd6175a7bd31d5")

    def url_for_version(self, version):
        return f"https://github.com/vanheeringen-lab/ANANSE/archive/refs/tags/v{version}.tar.gz"

    # Python and build system
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # Runtime dependencies from setup.py install_requires
    depends_on("py-adjusttext", type=("build", "run"))
    depends_on("py-dask@:2023.9.1", type=("build", "run"))
    depends_on("py-genomepy@0.14:", type=("build", "run"))
    depends_on("py-gimmemotifs@0.18:", type=("build", "run"))
    depends_on("py-loguru", type=("build", "run"))
    depends_on("py-matplotlib@3.3:", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-numpy@1.6:", type=("build", "run"))
    depends_on("py-openpyxl", type=("build", "run"))
    depends_on("py-pandas@:1", type=("build", "run"))  # < 2
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pydot@1.4.1:", type=("build", "run"))
    depends_on("py-pygraphviz@1.7:", type=("build", "run"))
    depends_on("py-pyranges", type=("build", "run"))
    depends_on("py-tables", type=("build", "run"))  # aka pytables
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy@1.9:", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # Basic import test to validate installation
        with working_dir("spack-test", create=True):
            python("-c", "import ananse")

