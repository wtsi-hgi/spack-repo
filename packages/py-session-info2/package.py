# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySessionInfo2(PythonPackage):
    """Print versions of imported packages."""
    
    homepage = "https://session-info2.readthedocs.io/"
    pypi = "session-info2/session_info2-0.2.3-py3-none-any.whl" 

    version("0.1", sha256="f45d6873d5eb57910aa7920b0acd7a021777a6a53d7f974a0fd9cc5c18e20e81", expand=False, url="https://files.pythonhosted.org/packages/4b/c4/83e7eab89c064305374af25907bc4573b047e950f925e508fedde78af158/session_info2-0.1-py3-none-any.whl")
    version("0.1.1", sha256="86609fd1006cbb15afa38ecd8ce9cd657b234f18f12824a3a1cfa03692c51eac", expand=False, url="https://files.pythonhosted.org/packages/10/6a/23cf598924cc60b939dfa6696e7bd2284372b02ebdfea4916d8007c45d61/session_info2-0.1.1-py3-none-any.whl")
    version("0.1.2", sha256="8f5c010b621930556eee640f6a71d76f0c746ed1194b27ad227e6fe6e61883d4", expand=False, url="https://files.pythonhosted.org/packages/db/98/9578ce1d8ae951cf44e6b7434854824f0eae12d54b270e80014f8ab1971c/session_info2-0.1.2-py3-none-any.whl")
    version("0.2", sha256="4e1a39ab1d791e0c2967dca9d0f69f243c6821e0319a9fc68f8428ec8e8aa54f", expand=False, url="https://files.pythonhosted.org/packages/e0/e4/1e32328d993d0c7d24e5acc9a6f0f205a4a70e46c8cc35f0a64bae899889/session_info2-0.2-py3-none-any.whl")
    version("0.2.1", sha256="2554f974441fe5a230d45ef5389cfaf663af7ff41520b488a633c03743f34658", expand=False, url="https://files.pythonhosted.org/packages/91/a2/8575bc8036ee4f96043cd6b4433b3adc120aa365a6b7aef19f564c99cbb7/session_info2-0.2.1-py3-none-any.whl")
    version("0.2.2", sha256="3284dc1e6e3fc423770681498bbfea4b1992db756bd0400288aad693d000583d", expand=False, url="https://files.pythonhosted.org/packages/89/69/1e43007a356af28c95ca92a877cabec2b18a0f9484c2480677c0d590ed62/session_info2-0.2.2-py3-none-any.whl")
    version("0.2.3", sha256="f211d9930f73b485b727b6c4d8b964fa1b634351b3079393738f42be9b4c7f5e", expand=False, url="https://files.pythonhosted.org/packages/9d/b7/7d4c95c7b8525dabea23c548a1bb068d7a61635d544e8c92c51e784dad63/session_info2-0.2.3-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))

# {"furo;extra=='docs'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "hatch;extra=='docs'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "myst-nb;extra=='docs'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "session-info;extra=='docs'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "sphinx;extra=='docs'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "ipywidgets;extra=='jupyter'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "ipywidgets;extra=='notebook'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "numpy;extra=='notebook'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "session-info;extra=='notebook'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "coverage[toml]>=6.5;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "ipykernel;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "jupyter-client;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "pytest;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "pytest-asyncio;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "pytest-md;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "pytest-subprocess;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "testing-common-database;extra=='test'": ['0.1', '0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "ipywidgets;extra=='docs'": ['0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "numpy;extra=='docs'": ['0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "sphinx-autodoc-typehints;extra=='docs'": ['0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "sphinx-codeautolink;extra=='docs'": ['0.1.1', '0.1.2', '0.2', '0.2.1', '0.2.2', '0.2.3'], "click!=8.3;extra=='docs'": ['0.2.3']}