# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLineedit(PythonPackage):
    """An readline library based on prompt_toolkit which supports multiple modes"""

    homepage = "https://github.com/randy3k/lineedit"
    pypi = "lineedit/lineedit-0.1.6.tar.gz"

    version("0.0.1", sha256="048d036f5099f9336799bb5064ac185e1c237181b26393ff5a98e500f22d15ab")
    version("0.0.2", sha256="1f16e409fd0ba412580619b10546d892d12a031a02fc6e4f6c7a3369a38a2357")
    version("0.0.3", sha256="9f14f37d914111a71aa861f0d5624587bddcf2bfd13599422b11b0e78d1fce9b")
    version("0.0.4", sha256="a6a4c556b8da2155e030c89bb10e95acdfad71e300b5d828e95697e39860f027")
    version("0.0.5", sha256="ddb1f3bc1ce64fc2c98cceb5f26f49a0eada54e09ec53008910f30e18ce31b98")
    version("0.1.0", sha256="739687119a9735ede6b1b08cfa62c41abfa91735d67641bf41d10f160c5c1d30")
    version("0.1.1", sha256="1000583c0adb16a8fde859d8eb026bfc499a370ee51bdae445dc037180683c3d")
    version("0.1.2", sha256="84732d45ada6ac645db6349deecd0611b1c0fc9169bb1d6a669f2b15d8ef4257")
    version("0.1.3", sha256="5b9f9a9cab1d1747c30515b4d2b1233572532303066532f435edfeaceb6247ac")
    version("0.1.4", sha256="c2d4bb5cd442fcb1442cd7b368ad1013b05d884366e8c9c4d46cd0f1376545fc")
    version("0.1.4.dev0", sha256="5b76fd708b51dfa0de9366637db8dedeac4c6346d9ea526e086d939d35c0382c")
    version("0.1.5", sha256="feef1347bf9e460a5082dafb05ad9c13bd49ad27b04174d07379a13c37f6fd40")
    version("0.1.6", sha256="f4795479154e350ad9cf6e8be6ad3a78f10f892b99675af2f8140f2d847f6f3f")

    depends_on("py-setuptools", type="build")
    depends_on("py-pygments", type=("build", "run"))
    depends_on("py-six@1.9:", type=("build", "run"))
    depends_on("py-wcwidth", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = which("python")
            python("-c", "import lineedit")
