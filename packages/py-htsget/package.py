# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHtsget(PythonPackage):
    """Python API and command line interface for the GA4GH htsget API."""
    
    homepage = "http://pypi.python.org/pypi/htsget"
    # Prefer wheels where available
    pypi = "htsget/htsget-0.2.6-py2.py3-none-any.whl" 

    version("0.1.0", sha256="de13f881033b67e5c0effc9ef995e65370c9de5afe5f844f4614dfd0453585b7")
    version("0.1.0a1", sha256="47a4597ec016e1b08ca8d7daaf32f91002b2d28c335b9cf68177ec6c1d8d5f31")
    version("0.1.0a2", sha256="709039c15c56bb915b8657fba1a39ede04c18db775e7e7757c16b1d29516a405")
    version("0.1.0a3", sha256="4154ddccfafcce7f7d95c79de50b1e83dd7a5eadef6f4a95a9cc7a5a2445339c")
    version("0.1.0a4", sha256="e12f110d4bfbe4a0939b87fecb8236c326cc43e8734e5dae381c97dc7b5d1d19")
    version("0.1.0a5", sha256="4d7a05000f626ed16b3c60eb2ee47b97748ae77e87d8c3cb49d1ad4b27f29a9d")
    version("0.1.1", sha256="98e225c19496eb36c1f199c4f34934c0c38c42aca315c235a1c54119c85561a1", expand=False, url="https://files.pythonhosted.org/packages/aa/1d/4e088d3148ad6dcca525023a33a9a9417d1df30cff7c7accba1e3c691a2b/htsget-0.1.1-py2.py3-none-any.whl")
    version("0.1.2", sha256="af492cf35738b958f1092804d5f99fbd2691c30e3d4b2d867152dec5b8692210", expand=False, url="https://files.pythonhosted.org/packages/31/ab/6de4b9757c8953fc562ef4c5c5af64436adbfdd3d1788ac1d6f05d5677e3/htsget-0.1.2-py2.py3-none-any.whl")
    version("0.2.0", sha256="aa9af42361756379ffdc8a044332ba68987191b5e65dde9e8069cf57fa26183a", expand=False, url="https://files.pythonhosted.org/packages/af/31/872332719cca49a2037aa6cede0ab26ffe92cddeeb98758953f5fce07a2d/htsget-0.2.0-py2.py3-none-any.whl")
    version("0.2.1", sha256="51fd211227faa6b21a027803a8e0ec36ee7fbeac4dd95f0aa621089c2f703e32", expand=False, url="https://files.pythonhosted.org/packages/ee/5e/035c8da41bf2c7580a0e7a8427f4046d731fb0270d4009978943bea743fa/htsget-0.2.1-py2.py3-none-any.whl")
    version("0.2.2", sha256="2345679dacedc54b86b49637fb311874f5cac08429f57fec0548850e7a9dffad", expand=False, url="https://files.pythonhosted.org/packages/c3/a2/7cdd6477cb46d4a004c9699dc83f485663e64e61f7388f639d9d8cafbd72/htsget-0.2.2-py2.py3-none-any.whl")
    version("0.2.3", sha256="fed933326b8caa5e387acd686de0c92862261746db0c29e0743fd03714f5ee66", expand=False, url="https://files.pythonhosted.org/packages/f5/9a/d113ad9f27dbb459a61c6bc6bfa82e3d76dafe85bc59b2c25fc9e5bf35e7/htsget-0.2.3-py2.py3-none-any.whl")
    version("0.2.4", sha256="7ac8b6ece7a5942a93ff3f0f58daaea2e0b1821b1ede01d003f116ee9fae9727", expand=False, url="https://files.pythonhosted.org/packages/d5/74/59e97dddf9b100c5a4502300a300fd3214f1aa0bfc58db4dd2c4a01f2e85/htsget-0.2.4-py2.py3-none-any.whl")
    # Use sdist for 0.2.5 to allow normal source expansion
    version("0.2.5", sha256="d383dc36f699bd921f760f5500c8ed251e5f8358a7cc219c6c89c35d103e8045", url="https://files.pythonhosted.org/packages/99/23/dedd2de16464cff36870019c7894cdbae83f121ab479121ababbef2add48/htsget-0.2.5.tar.gz")
    version("0.2.6", sha256="0cca50c9aa6708c5a1d1df10b557fcac7100266ad64a78555337a357f02148a0", expand=False, url="https://files.pythonhosted.org/packages/c0/37/74d124fbdc0e04e552e7f0ba2a8c8594b5caa82ac10c4d80fe277beb15e9/htsget-0.2.6-py2.py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-humanize", type=("build", "run"))

# {'requests': ['0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.6'], 'six': ['0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.6'], 'humanize': ['0.2.3', '0.2.4', '0.2.6']}