# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWadlerLindig(PythonPackage):
    """A Wadler–Lindig pretty-printer for Python."""
    
    homepage = "https://docs.kidger.site/wadler_lindig/"
    pypi = "wadler-lindig/wadler_lindig-0.1.7-py3-none-any.whl" 

    version("0.1.0", sha256="3fa7649704fa68d32afaa66afc04f6fca258f070ea0de541784039102cbd487a", expand=False, url="https://files.pythonhosted.org/packages/63/ee/778b26f76765582672c5b589396c8a9595bfe2d5a762a261a4cef91afd2e/wadler_lindig-0.1.0-py3-none-any.whl")
    version("0.1.1", sha256="3998cf541216ce46d5201188b42c3545023d18a25af9cd601c8b6ae6c0b9200b", expand=False, url="https://files.pythonhosted.org/packages/35/13/f015debe8dc449a898cbc844160ec660df4c290a680d3c6849e64ddb2cb1/wadler_lindig-0.1.1-py3-none-any.whl")
    version("0.1.2", sha256="c4a003aaff91ab8da45b7660918f8203800b5b69efefffa223bcfc785bb7be0e", expand=False, url="https://files.pythonhosted.org/packages/26/de/4ee24291c8538b70250aad405e4cf911610f5091ae4d54aad3ce087c8d72/wadler_lindig-0.1.2-py3-none-any.whl")
    version("0.1.3", sha256="3018e4e6b115a7ef21c77414a41cbe7e03e83f6b5e25004958e33432a17f3c94", expand=False, url="https://files.pythonhosted.org/packages/39/3b/5b918a0da0d6920e7f7328cf0ab00df31b905d709f458596304f09096785/wadler_lindig-0.1.3-py3-none-any.whl")
    version("0.1.4", sha256="5c463aeb1f4ddc4acc12c3708d22ae21bcfc3e19e7c4d7aeef6642ea57b1a8b8", expand=False, url="https://files.pythonhosted.org/packages/7b/69/cfb1af44622044d4db0cad65721d283a921a4795f0ad121616b9eaa6ccd7/wadler_lindig-0.1.4-py3-none-any.whl")
    version("0.1.5", sha256="54f830ec0bdab41b28df8bc91be4596c6cc8cf9772b3b5c7cd5922d2ba5073b7", expand=False, url="https://files.pythonhosted.org/packages/f9/4e/ef53ee4a6bf563a7c0a33682d6fef7a96b6685821516e52596cd90a376cd/wadler_lindig-0.1.5-py3-none-any.whl")
    version("0.1.6", sha256="d707f63994c7d3e1e125e7fb7e196f4adb6f80f4a11beb955c6da937754026a3", expand=False, url="https://files.pythonhosted.org/packages/d1/9a/937038f3efc70871fb26b0ee6148efcfcfb96643c517c2aaddd7ed07ad76/wadler_lindig-0.1.6-py3-none-any.whl")
    version("0.1.7", sha256="e3ec83835570fd0a9509f969162aeb9c65618f998b1f42918cfc8d45122fe953", expand=False, url="https://files.pythonhosted.org/packages/8d/96/04e7b441807b26b794da5b11e59ed7f83b2cf8af202bd7eba8ad2fa6046e/wadler_lindig-0.1.7-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))

# {"numpy;extra=='dev'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], "pre-commit;extra=='dev'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], "pytest;extra=='dev'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], "jinja2==3.0.3;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocs-autorefs==1.0.1;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocs-include-exclude-files==0.0.1;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocs-material-extensions==1.3.1;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocs-material==7.3.6;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocs==1.3.0;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mkdocstrings==0.17.0;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "mknotebooks==0.7.1;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "nbconvert==6.5.0;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "nbformat==5.4.0;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "pygments==2.14.0;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "pymdown-extensions==9.4;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "pytkdocs-tweaks==0.0.8;extra=='docs'": ['0.1.0', '0.1.1', '0.1.2', '0.1.3'], "hippogriffe==0.1.0;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "mkdocs-include-exclude-files==0.1.0;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "mkdocs-ipynb==0.1.0;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "mkdocs-material==9.6.7;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "mkdocs==1.6.1;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "mkdocstrings[python]==0.28.3;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7'], "pymdown-extensions==10.14.3;extra=='docs'": ['0.1.4', '0.1.5', '0.1.6', '0.1.7']}