# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGprofilerOfficial(PythonPackage):
	"""Functional enrichment analysis and more via the g:Profiler toolkit"""
	
	homepage = "https://biit.cs.ut.ee/gprofiler/"
	pypi = "gprofiler-official/gprofiler_official-1.0.0-py3-none-any.whl" 

	version("0.1", sha256="72dceb37401b1b6b0455cb10fd822119c7180cc17ff51679cd8adc1e729d2746")
	version("0.1.1", sha256="baea739254c94411395c4b5e37d06c7440af5c24b1b70b4a2e72d52764646b8b")
	version("0.2.1", sha256="fb8a5cdc93e35a27e00184b9ffd014809d240974b40a4ade699f8d803f948249")
	version("0.2.2", sha256="024c7446879fb0a07b9bbe500cafebf67367b99e3a34c6c10c784f879b63e755")
	version("0.2.3", sha256="6e5101b15daf624f7a592b6f3de826d9154e2f697a40c3ec73bee8bc06c093ef")
	version("0.3", sha256="2b8a76cc98aaed08ef8ad2ce9ccd7ac653460402011027dbd62dd7ed4b8121b4")
	version("0.3.3", sha256="a9ad85b9c642617fa046dd56a217e820878f28652dfe088cbeb5ed2516d2dc7d")
	version("0.3.4", sha256="fc4218d561925ca287e5bad88408e067ccade3c3ce898bcb27cf35aba07b6cd8")
	version("0.3.5", sha256="64facf0d7bcbf91e69ad4c0d736d9e2378024f12b772bc330618a08b9f4fc20d")
	version("1.0.0", sha256="c582baf728e5a6cddac964e4085ca385e082c4ef0279e3af1a16a9af07ab5395", expand=False, url="https://files.pythonhosted.org/packages/df/1b/5a87c1a1da8f601c00a0ce4dedb5aab8a5cad6a0f4a5062c4da22a045072/gprofiler_official-1.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-requests", type=("build", "run"))

# {'requests': ['1.0.0']}