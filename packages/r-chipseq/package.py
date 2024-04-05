# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseq(RPackage):
	"""A package for analyzing chipseq data,

	Tools for helping process short read data for chipseq experiments"""

	bioc = "chipseq"

	maintainers("dorton21")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/chipseq_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/chipseq/chipseq_1.52.0.tar.gz"]
	version("1.52.0", md5="5cf8ab297fc95d0a36b4359488c50358")
	version("1.50.0", commit="0bdfa25828b1d65f629e96c8e832061fd7ff7935")
	version("1.48.0", commit="9c78296001b6dd4102318879c8504dac70015822")
	version("1.46.0", commit="76b00397cd117d5432158f50fc1032d50485bd24")
	version("1.44.0", commit="b64d0d28e9fcf0fdab9a7f9c521baf729426a594")
	version("1.40.0", commit="84bcbc0b7ad732730b5989a308f1624a6a358df1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
