# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRutledge(RPackage):
	"""Real-Time PCR Data Sets by Rutledge et al. (2004)

	Real-time quantitative polymerase chain reaction (qPCR) data
    by Rutledge et al. (2004) <doi:10.1093/nar/gnh177> in tidy format. The
    data comprises a six-point, ten-fold dilution series, repeated in five
    independent runs, for two different amplicons. In each run, each standard
    concentration is replicated four times. Original raw data file:
    <https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nar/32/22/10.1093_nar_gnh177/1/gnh177_Supplementary_Data.zip?Expires=1680370010&Signature=xxk4VxX0C4yr3UWzxgh7ieCt7QQmpFMRauvsVEwtGXYGCcyQY7uhNCE-M8zx9kpyDPoS8NR7fjBuMx2Xz2ANFwF1VqnjQ4AfO37klnJ3CHRIJ7bj01n2mycHDnvJ3XawHdWT8TqJxTxVC9CpYEkH2xGeJBnnpcnXLbc94A8KB8FCtg2WR3O~ULkaOQQ8uJAiVdJhnBHH~XfBRkfoKHSuyJgX7n7M2~gwXnZH9n3vUyo~CHrpIax7Hi0xUSCBbQM571hxA7JIHkhZ0HBm2aXFuAru2yJ~o8jMEnnguOJg8T7mGqTDzUBtW0hJhmQDksdJoyeAFzU84QRUIZj9q3-tXg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA>.
	"""
	
	homepage = "https://github.com/ramiromagno/rutledge"
	cran = "rutledge" 

	version("0.1.0", md5="f54236983d7ec6308b3ec444db3f8429")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
