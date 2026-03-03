# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAioeasywebdav(PythonPackage):
	"""A straight-forward WebDAV client, ported from easywebdav to use aiohttp."""
	
	homepage = "https://gitlab.com/alelec/aioeasywebdav"
	pypi = "aioeasywebdav/aioeasywebdav-2.4.0-py3-none-any.whl" 

	version("2.0.0", sha256="42c9d50769207ff3a6b9c7b56e8830000c4656a30a01bd94d2df02766426b193")
	version("2.1.0", sha256="3be5d9a0a88d5fd1db4143ca62c03585c4c0300787e46f5930c611e5a9e86e58")
	version("2.2.0", sha256="2645934033bf2788ac962123d223e853fdbb0425127080e86b43be58d5d2545f")
	version("2.3.0", sha256="c4e25a76b22160ac2c02eee50e362f8bed5c3eea0528a17b3d9c657c11166ba9", expand=False, url="https://files.pythonhosted.org/packages/e8/a5/a6ba8b485cdc9a27c32f2989f3f703fceef1908cba0bfe13474544845564/aioeasywebdav-2.3.0-py3-none-any.whl")
	version("2.4.0", sha256="e4b760697ba23831bff41f2e9ce37b46dd9503d8aa0ba8d6e680842879ebb603", expand=False, url="https://files.pythonhosted.org/packages/5b/c6/761700c7748252cf1e73f6b11238d74ee786d833c06fe1d13260f3f1e3aa/aioeasywebdav-2.4.0-py3-none-any.whl")

	depends_on("py-setuptools-scm", type=("build", "run"))
	depends_on("py-six", type=("build", "run"))
	depends_on("py-aiohttp", type=("build", "run"))

# {'aiohttp': ['2.3.0', '2.4.0'], 'six': ['2.3.0', '2.4.0'], 'setuptools-scm': ['2.3.0', '2.4.0']}