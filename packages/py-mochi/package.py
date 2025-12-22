# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMochi(PythonPackage):
    """MoCHI fits mechanistic models to deep mutational scanning data with neural networks."""

    homepage = "https://github.com/wtsi-hgi/MoCHI"
    git = "https://github.com/wtsi-hgi/MoCHI.git"

    license("MIT")

    version("20251222", commit="3c4a8da11ec270eacc41dcbe259539ef0e8e7963")
    version("1.1", git="https://github.com/lehner-lab/MoCHI.git", tag="v1.1")
    version("1.0", git="https://github.com/lehner-lab/MoCHI.git", tag="v1.0")

    depends_on("py-setuptools", type="build")
    # Python 3.12+ removes distutils which joblib (via scikit-learn) still imports
    depends_on("python@3.9:3.11", type=("build", "run"))

    depends_on("py-numpy@1.21:1.23", type=("build", "run"))
    depends_on("py-pandas@1.4:", type=("build", "run"))
    depends_on("py-matplotlib@3.5:", type=("build", "run"))
    depends_on("py-pyreadr@0.4.4:", type=("build", "run"))
    depends_on("py-torch@1.10:", type=("build", "run"))
    depends_on("py-scikit-learn@1.0:", type=("build", "run"))
    depends_on("py-scipy@1.8:", type=("build", "run"))
    depends_on("py-seaborn@0.11:", type=("build", "run"))

    def patch(self):
        # Versioneer still references SafeConfigParser which was removed in Python 3.12
        filter_file(
            "configparser.SafeConfigParser",
            "configparser.ConfigParser",
            "versioneer.py",
            string=True,
        )
        filter_file(".readfp(", ".read_file(", "versioneer.py", string=True)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import pymochi")
