# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAntipickle(PythonPackage):
    """Like pickle. But different"""
    
    homepage = "None"
    pypi = "antipickle/antipickle-0.2.0rc0-py3-none-any.whl" 

    version("0.2.0", sha256="16e437f59f24c6608629aeeca2eaf831951d718bf55fdfe3bed6be84912c91da", expand=False, url="https://files.pythonhosted.org/packages/41/72/e86064a1c2b820eedf07bfd8d66cb5ed5063ad6b0325de3b94edb7cbd4f4/antipickle-0.2.0-py3-none-any.whl")
    version("0.2.0rc0", sha256="fb36ee2c6e40229f8eb1874d210aaba51bf51b7577a534b30443c9041bbd1181", expand=False, url="https://files.pythonhosted.org/packages/fb/36/da8f26bb6a580985c82f54fe7f62faba57cb66a8df1c38d55da44bfc13e1/antipickle-0.2.0rc0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.7:", type=("build", "run"))

# {'msgpack>=1.0.4': ['0.2.0', '0.2.0rc0']}