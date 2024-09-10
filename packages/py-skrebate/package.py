# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySkrebate(PythonPackage):
	"""Relief-based feature selection algorithms"""
	
	homepage = "https://github.com/EpistasisLab/scikit-rebate"
	pypi = "skrebate/skrebate-0.7.tar.gz" 

	version("0.1", sha256="31fdfe20fcff09ce09dd5e1391e635429a1d3c0f1684511e562507b609db42d2")
	version("0.2", sha256="a64610d242648849dac7d9f049ba8ca9bab1d692b0e29942bffefa63ef980d54")
	version("0.3", sha256="e238b98dfa588f3f5be22ffa5d17bb1051fb6dba61f949ef6f2e3267a5d5f553")
	version("0.3.1", sha256="fe2e5419fe65deda4e296b0cd00f4bd69962f4dae010aab874f66e68abb34fb8")
	version("0.3.2", sha256="73b4bec79938a2b4e28769a8a97d00f9d01b627f5e0d0786a8219eaa62559460")
	version("0.3.3", sha256="c44f647a4decaa29e63bba9a49a8c749a99c0dd3ca5597365999453dc42d6cca")
	version("0.3.4", sha256="32fe726f9ebe1cf874f31d99b418c0aecc5707db2e4f846be50007a862d54375")
	version("0.4", sha256="e7311e2ef54461a2d6df4ac4c81d74dec9e71ccd02040bc7fadb3a5221225cc2")
	version("0.5", sha256="a07e1659e40d240ff8afab9c8a744cb6e0da69c3e60e6147fc441d8944918a6e")
	version("0.6", sha256="87c7192349302581c85bb1e119088e25d62bc7be35a305ff52f8df2e5fd2f8c0")
	version("0.61", sha256="cb4441e6833ecf5e359f9e1048e78abf7859d8a5da249df6a7d1c80c3b99a5b4")
	version("0.62", sha256="b20dad4dc52f650e1f7960151314840f34251222cae0a78ac23d9f6d377ca558")
	version("0.7", sha256="88cf3302e2027d16b76f289a361515f569875be6f63aa2b0d547a3876ccde988")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
