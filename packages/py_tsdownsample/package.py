# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyTsdownsample(PythonPackage):
    """Time series downsampling in rust"""

    homepage = "https://github.com/predict-idlab/tsdownsample"
    pypi = "tsdownsample/tsdownsample-0.1.4.1rc0.tar.gz"

    version("0.1.0", sha256="adeeaa219773c4c5a7c29a50eac011e92ef76297debe334f09780db68c2181fb")
    version(
        "0.1.0a0",
        sha256="3c85d033776ecf569f90c46a8821dbb8020ad3875f79a56b18537d4850deee5e",
        expand=False,
        url="https://files.pythonhosted.org/packages/fa/ef/61e384a5b442db5d1f73d5ae5a875bac573492d799b21dc9f39daddac8b1/tsdownsample-0.1.0a0-py3-none-any.whl",
    )
    version("0.1.0a1", sha256="cab02e57e183b2e640a67f67d644569d9574e61f720502482f7303625b987f8a")
    version("0.1.0a2", sha256="79de0cd4bb55d09937fa3701811f5365d2a9ab31ce9c5612084b8341496c8717")
    version("0.1.0a3", sha256="b91c264268cd80863ee9b1c488836b5ae651fbb3ef8bcea85aeffee43f27cb2e")
    version("0.1.0a4", sha256="bdc226a337ed8dcbf4f57529fa7f2981f2373c9297da9931af4abae28c3f9549")
    version("0.1.0a5", sha256="a6c1f0270344b20d2654b4ccca2ef40ac731715e13163680204de15ee4c22bc9")
    version("0.1.0a6", sha256="f3639a14cce03b15167126a965eacd137e8d796a3659235150300b94191d5780")
    version("0.1.0a7", sha256="808485166e59000132103d552f6f2d2d50e75393dd22309b44f736f7fa600952")
    version("0.1.1", sha256="c7619017ed08376eefb59cacfa113e24a53c060624648b628ff624a88a48a415")
    version("0.1.2", sha256="9da0b8f8859e9651910cc150bc5115bf5d1890d8ebee12bf57bd1bb016a0112a")
    version("0.1.2a0", sha256="fdb3b352619be563feb4675657af028d9d26c9b3cac12a2b1b1b36c544648b75")
    version("0.1.2a1", sha256="8e67a4b77388ed21b85dee2bf281c1b0b0c9d3c60a5815dd9df31dc0f3f143d0")
    version("0.1.3", sha256="5268d0ab5e8572138871feff389440a0c59d5e0fe02c0fa1cf975d74ba33b933")
    version("0.1.3rc1", sha256="86c54b2acc0b17ed70f2e3c184a2a523ec054c466e6ffefff9739bad6e6040ac")
    version("0.1.3rc2", sha256="6da88a8b96c55909372e45dedfd7b0d012a9142ed8ffb145995906d60c40afc1")
    version("0.1.4.1", sha256="cc2e2fc0031a5fb75c0f5204b498e86eae0333bcc19da481c0859f1943690f3b")
    version("0.1.4.1rc0", sha256="31560df8d1ab621f7541cf7651ad3258bcbbf1933884eab4f11e5036c3468f49")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-maturin", type="build")
    depends_on("rust@1.81:", type="build")

    def patch(self):
        os.remove("Cargo.lock")


# {'numpy(>=1.21)': ['0.1.0a0'], 'pandas(>=1.3)': ['0.1.0a0']}
