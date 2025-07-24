# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEinx(PythonPackage):
    """Universal Tensor Operations in Einstein-Inspired Notation for Python"""
    
    homepage = "https://github.com/fferflo/einx"
    pypi = "einx/einx-0.3.0-py3-none-any.whl" 

    version("0.0.1", sha256="973447cb412a3b19e729884f190d125d7d409cbc24781dcf00120f77a71ce7f1")
    version("0.0.2", sha256="190520e2a8b23d6dd7ae2dda528e7f40e9fe94955b2b0fbb6b88422e61273dd0")
    version("0.0.3", sha256="8fae6dc7d210e6c49f2060ee0b4ed5ccc9738f1bf3736924d9211222d7474f49")
    version("0.1.0", sha256="c06289aa0b40d4d3fc9f0240a02fe314ab6b5df546b3175b9c32afb26752e421")
    version("0.1.1", sha256="84b834177491b40f6cc7524f269500b62134c2e776aa1467753cbd26107e51ff")
    version("0.1.2", sha256="512e70cc818a842d10185ae159a92b9965b5f096a263b01d928c8df55e75126e")
    version("0.1.3", sha256="b614e6749dfd8dc24eb35c555b4bd7bd7cdf09b2e740943d115fb6cc9d21bded", expand=False, url="https://files.pythonhosted.org/packages/ec/b5/fdb2fe8d49bf812b0e3f5ee32c4ae53abe98cb6e7cd5013c7987f0fe36c4/einx-0.1.3-py3-none-any.whl")
    version("0.2.0", sha256="153b2d8a70dd29dc32d2376b44b99d8d528a6b89c5172ac8d97c0f867a870069")
    version("0.2.1", sha256="df66c68ab4eaf593b70252eaca34a48a44d711ce7733b4a779ce783387d062dc", expand=False, url="https://files.pythonhosted.org/packages/4e/42/280fe2424e39b5611d017033567a065f79a2eaa43cf02f236aa07ccda448/einx-0.2.1-py3-none-any.whl")
    version("0.2.2", sha256="bde86f19a60bc8ce3c3aa173c0f1ba59df8d8c0435c4b61638499c3d187dd28b", expand=False, url="https://files.pythonhosted.org/packages/08/b7/69d8d5a187fa8d86dec7357d63fbd36eaf9cf3f5e62adc169148d569384b/einx-0.2.2-py3-none-any.whl")
    version("0.3.0", sha256="367d62bab8dbb8c4937308512abb6f746cc0920990589892ba0d281356d39345", expand=False, url="https://files.pythonhosted.org/packages/90/04/4a730d74fd908daad86d6b313f235cdf8e0cf1c255b392b7174ff63ea81a/einx-0.3.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))
    depends_on("py-frozendict", type=("build", "run"))

# {'numpy': ['0.1.3', '0.2.1', '0.2.2', '0.3.0'], 'sympy': ['0.1.3', '0.2.1', '0.2.2', '0.3.0'], 'frozendict': ['0.1.3', '0.2.1', '0.2.2', '0.3.0'], "keras>=3;extra=='keras'": ['0.1.3', '0.2.1', '0.2.2', '0.3.0'], "torch>=2;extra=='torch'": ['0.1.3', '0.2.1', '0.2.2', '0.3.0']}