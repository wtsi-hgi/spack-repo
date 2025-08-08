# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSf(RPackage):
	"""Simple Features for R.

	Support for simple features, a standardized way to encode spatial vector
	data. Binds to 'GDAL' for reading and writing data, to 'GEOS' for
	geometrical operations, and to 'PROJ' for projection conversions and datum
	transformations. Optionally uses the 's2' package for spherical geometry
	operations on geographic coordinates."""

	cran = "sf"
	version("1.0-9", sha256="85c0c71a0a64750281e79aa96e36d13e6285927008b2d37d699e52aba7d8013b")
	version("1.0-8", sha256="3ddc7090e79d6b5e3fad69e01254677ab5ec86a0b25e7e73493c8eac0ea98732")
	version("1.0-7", sha256="d0731fab9438d73a55af7232f0474b36f4b2a4e6d66adaa141632f4a60265453")
	version("1.0-5", sha256="290c28fa5ea777d555e70962c59079c134f02f7bdf60259a72eea79a064a1ac4")
	version("1.0-16", md5="23f6a4017327db84e4f5b28807ccf962")
	version("1.0-15", md5="b3c5d978da86e8da20f577b65c4eaaff")
	version("1.0-12", sha256="3778ebf58d824b1dfa6297ca8363714d5d85eda04c55ab2bf39597cac1d91287")
	version("0.9-7", sha256="4acac2f78badf9d252da5bf377975f984927c14a56a72d9f83d285c0adadae9c")
	version("0.7-7", sha256="d1780cb46a285b30c7cc41cae30af523fbc883733344e53f7291e2d045e150a4")
	version("0.7-5", sha256="53ed0567f502216a116c4848f5a9262ca232810f82642df7b98e0541a2524868")
	version("0.5-5", sha256="82ad31f98243b6982302fe245ee6e0d8d0546e5ff213ccc00ec3025dfec62229")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-classint@0.4.1:", type=("build", "run"))
	depends_on("r-dbi@0.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s2@1.1:", type=("build", "run"))
	depends_on("r-units@0.7.0:", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))

	def setup_build_environment(self, env):
		# Ensure R headers are on the include path for configure tests
		r_include = join_path(self.spec['r'].prefix, 'rlib', 'R', 'include')
		env.append_flags('CPPFLAGS', f"-I{r_include}")
		env.append_flags('CFLAGS', f"-I{r_include}")
