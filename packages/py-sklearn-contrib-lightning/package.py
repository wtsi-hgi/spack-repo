# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySklearnContribLightning(PythonPackage):
    """Large-scale sparse linear classification, regression and ranking in Python"""

    homepage = "https://github.com/scikit-learn-contrib/lightning"
    pypi = "sklearn-contrib-lightning/sklearn-contrib-lightning-0.6.dev0.tar.gz"

    version("0.1.1", sha256="562327371acc4b24aeb1c155e3cf0ea5773364ab5afd3112bceecfc291028482")
    version("0.2.0", sha256="ca0604bdbcb835b6ba2e3472d503717980c9be4eb95a94f06da5736fdec5499b")
    version("0.3.0", sha256="d286e91e37bad736984265d3967a1dcc05417e13b1fb7057eb277e6e31399cab")
    version("0.4.0", sha256="43c1d7fe2b448fc0154da0bb3e107511eb5d3977427ac35ace01fa101bd99c71")
    version("0.5.0", sha256="fc27cd40bb81faf4cc1fe91d983c87097dd323afbf0935b51beaa3fe1835c09d")
    version("0.6.0", sha256="ec21510ebc4f472a757b441eccb796398b193966c431b8178a1d52509d73a76e")
    version("0.6.1", sha256="72579fcf2df9b546997baa5e271f28adf898b5f68c6c6c718bbb53ea15d011c5")
    version("0.6.1.dev0", sha256="054f190558de372db6658b9b39ccbb7f346a03bd8bc729d6a6b6256410f6c186")
    version("0.6.2", sha256="d0de4b061f068665a1ec308b136e3c7f199dbcdff200318573efda5e11739eb8")
    version("0.6.2.post0", sha256="ace82cfd672f6d5be952780cae239650999ff9f1f750be7d62b43d905e33d6c1")
    version("0.6.dev0", sha256="8803f33d3b6d61f4bb7a974f4b21cf9d1cf182863401ab0f9f4f8b8d12358258")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
