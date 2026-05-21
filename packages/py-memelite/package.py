# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMemelite(PythonPackage):
    """Biological sequence analysis for the modern age."""
    
    homepage = "https://github.com/jmschrei/memesuite-lite"
    pypi = "memelite/memelite-0.2.0-py3-none-any.whl" 

    import_modules = ["memelite"]

    version("0.1.0", sha256="a953b55b1bb36bad5ebd042bff91a4d4e9008edfa2b1cf1d50cb546bea43ea86", expand=False, url="https://files.pythonhosted.org/packages/10/85/2c4701a250bb3a4a1abb98827f9a048597905c37f4cd129f7a5a36556228/memelite-0.1.0-py3-none-any.whl")
    version("0.2.0", sha256="6ccb38963e09b938b8412a05cab8244caa87e03e44c9c985af6a913b0d2ef5f0", expand=False, url="https://files.pythonhosted.org/packages/93/84/648dc9326dbb31d2dbcbe30d089f2f126a274f8e0b8a539818b9d1bd6f55/memelite-0.2.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-numba")
        depends_on("py-pandas")
        depends_on("py-pyfaidx")
        depends_on("py-tqdm")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import memelite")

# {'numpy<=2.0.1,>=1.14.2': ['0.1.0', '0.2.0'], 'numba>=0.55.1': ['0.1.0', '0.2.0'], 'pandas>=1.3.3': ['0.1.0', '0.2.0'], 'pyfaidx>=0.7.2.1': ['0.1.0', '0.2.0'], 'tqdm>=4.64.1': ['0.1.0', '0.2.0']}
