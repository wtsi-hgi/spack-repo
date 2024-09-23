# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUpsetplot(PythonPackage):
	"""Draw Lex et al.'s UpSet plots with Pandas and Matplotlib"""
	
	homepage = "https://upsetplot.readthedocs.io"
	pypi = "upsetplot/UpSetPlot-0.9.0.tar.gz" 

	version("0.1", sha256="7e28d24dd8fc71cb7de6630314e850bb325ac5bbe745b08944ffcfacd9e2607a")
	version("0.1a0", sha256="68097f04a964984faeba53324b22628c03b3ac6656ad151462f48465c7b11c44")
	version("0.1a1", sha256="53596af6efbe485f364e215418277ccc132e644b82abae17593692a7ff2d10d6")
	version("0.1a2", sha256="274a1f85809a36fa8436f4a9d7f0f0bc89dbdb2f58235cc6b43d5bad0418e8ce")
	version("0.1a3", sha256="b8cc5b78d4f9b7a130825494ece101a43995f5a375b5eb1ea46e3b81861c190c")
	version("0.2.0", sha256="b24ef42f652e138db0dbb3754abd92f812bb605c98c300ba47582f5f6caf957f")
	version("0.2.1", sha256="c0c78bb1c4f5f7d0c9be5fd95408e3b8ac250a8cf1161ce250e2c4e4e21077a2")
	version("0.3.0", sha256="0ad40e6c5bc614bb38dff10d1c4a12ab3e20ea2f978ada8d67ba5ad3bbf195f2")
	version("0.3.0.post1", sha256="d0bdb5397e7f15900cd9ea143796b03adc3843b6c7a291478643c9e7c940f6f1")
	version("0.3.0.post2", sha256="7ce4c9c35512bf2b230d57a8caceddcd30f1ab05f1b303e9cf8d3c7a4b5cffb4")
	version("0.3.0.post3", sha256="f433270bf1433f08383cf6fa882b47ec4fdd0bdf4462d0be9526b78c4bb4612f")
	version("0.4.0", sha256="9f3cbd012ed89866cc7d494c6e37b320eec4e14400d3e4c35d916f13aa9b5c7c")
	version("0.4.1", sha256="c1e23af4d90ca88d024cdea45dc3a84591cd97a80a6a3dfc18b5e7ad2b93944f")
	version("0.4.2", sha256="fe75a7dd017d20200490837076dc96884a672b7e048a9079187ffb8632e95e6c")
	version("0.4.4", sha256="d1895f5e9efaa16f3a7d5aa81b6ac03eda23e8f8a9dca348871e38a6a6887532")
	version("0.5.0", sha256="d1eb8b48ab53fac19fd0a478666a285b8463f7e6de5fc4fdbb1039a92bddf6cb")
	version("0.6.0", sha256="542875e306257a3f79bd36aacf1abc99bfe440b5da56d2af2e1c8065f9f4f987")
	version("0.6.1", sha256="b198f91a0454ff292788050347bd8da00bdc8fe17e2e9cfdd51ea6e59970adfb")
	version("0.7.0", sha256="a37e1bf19397212c2143b5004b83ecb7b0e144d1211bd2ec63654e57f87890f8")
	version("0.8.0", sha256="d470afe517bd10f3b08f95bba356da4b4f0593bcffdb76e65cdc8c8cd0e3927f")
	version("0.8.2", sha256="3d8b0ca0d48589f0fee19d7640f5805ecec76b4c9b4867938cdb23c52ccfedf5")
	version("0.9.0", sha256="95b76ac38c624c9dfb1eca1de1a37e30e07e83678b1c57839c943184247b8592")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
