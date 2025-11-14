# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAblang2(PythonPackage):
    """AbLang2: An antibody-specific language model focusing on NGL prediction."""

    homepage = "https://pypi.org/project/ablang2/"
    pypi = "ablang2/ablang2-0.2.1-py3-none-any.whl"

    version("0.1.0", sha256="a6636b66b0ea1aa5331dd8ea2564cf9b986aaebbca694a46e4566983518af7bd", expand=False, url="https://files.pythonhosted.org/packages/56/e7/75a9b777c87bb50bbb71ba8438a117636eb1b5e96de6d9b8800ae27b8d86/ablang2-0.1.0-py3-none-any.whl")
    version("0.1.1", sha256="b691f64c5a1090e7490d49059abc67ae634c268c45b7b4d5aa813e23a84389c9", expand=False, url="https://files.pythonhosted.org/packages/fc/5c/fc95963b488860bda8c476bfcd9b7b067b2c47880693d99421d0ee94bcc9/ablang2-0.1.1-py3-none-any.whl")
    version("0.2.1", sha256="eda9b550bd8d9bdf1caaac821c3951deff5ef7141d4644292c6ba09126bbd834", expand=False, url="https://files.pythonhosted.org/packages/c6/89/79e5964b73c6cf7a9b19bc8b7a9c727dedffd780086da92196cc6464d720/ablang2-0.2.1-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    # upstream requires torch>1.9
    depends_on("py-torch@1.10:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-rotary-embedding-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Fallback to a basic import test
            python("-c", "import ablang2")

# {'torch>1.9': ['0.1.0', '0.1.1', '0.2.1'], 'requests': ['0.1.0', '0.1.1', '0.2.1'], 'einops': ['0.1.0', '0.1.1', '0.2.1'], 'rotary-embedding-torch': ['0.1.0', '0.1.1', '0.2.1'], 'numpy': ['0.1.0', '0.1.1', '0.2.1']}
