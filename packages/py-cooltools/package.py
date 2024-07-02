# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCooltools(PythonPackage):
	"""Analysis tools for genomic interaction data stored in .cool format"""
	
	homepage = "https://github.com/open2c/cooltools"
	pypi = "cooltools/cooltools-0.7.0.tar.gz" 

	version("0.2.0", sha256="569ca46b035279289ac3af1fe5627b149feb239f29d649b1151e609a24b4a0ae")
	version("0.3.0", sha256="2a2518c163beaab05b4416df38c4aff7fc2a9dbb088214b30379af273bfe06dd")
	version("0.3.2", sha256="fa477e9edee4a4a44e4b0bf051481b95cfc81ca6651744102c7871186ccf72a9")
	version("0.4.0", sha256="24de6ae8039bc34aaa41f090093ef3f3869f55d107c5fa25c66f8bed88bc9ee7")
	version("0.4.0rc1", sha256="bed04c4104f3865818e4d7e9327a235be976d8b2c91405ddda5f2995cc890a2a")
	version("0.4.1", sha256="ec0819e0de67791ce915964b024b4940f56f47983d5834ea11879794bc99d4cd")
	version("0.5.0", sha256="7ec7eba5ca824407f1008ea392bdb3edd0f023a8dd4dedb5b57994b8c7a971ad")
	version("0.5.1", sha256="8fcc7339f9f7c66d312d22799aab3c92e7f4422c9767b3b73d287f3547fb1e22")
	version("0.5.2", sha256="49e60bab4aeeb983a239da90ea4dfad1470c1e5b39c363e480b93b03c47d7119")
	version("0.5.3", sha256="5be114a51cf3ecc957e661b254db1985cb1b0f1270bf40f0b1470e3284da0eb4")
	version("0.5.4", sha256="24cd25a52c03f9f2473aa33dc6a4729f28856cc8812f3f4aa8f7e792877d9ef3")
	version("0.6.0", sha256="ce970291b3b6b7d7abdd1c1fe374732491564866656e46e9a537cc7cf885a4a6")
	version("0.6.1", sha256="1082186215c1215b1f1192b1c5dd2d103e0db6df3dca3a9e49ec15676f5c0adb")
	version("0.7.0", sha256="8b26d4857cc76b2dd3d1097b85f828cf6d5f1cf85b0cfd4b67a310e33e7ece1c")

	depends_on("python@3.7.1:", type=("build", "run"))
	depends_on("py-scikit-image", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-numba", type=("build", "run"))
	depends_on("py-multiprocess", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-joblib", type=("build", "run"))
	depends_on("py-cython", type=("build", "run"))
	depends_on("py-cooler", type=("build", "run"))
	depends_on("py-click", type=("build", "run"))
	depends_on("py-bioframe", type=("build", "run"))
