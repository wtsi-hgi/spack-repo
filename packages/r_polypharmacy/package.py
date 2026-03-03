# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolypharmacy(RPackage):
	"""Calculate Several Polypharmacy Indicators

	Analyse prescription drug deliveries to calculate several indicators of polypharmacy corresponding to the various definitions found in the literature.
  Bjerrum, L., Rosholm, J. U., Hallas, J., & Kragstrup, J. (1997) <doi:10.1007/s002280050329>.
  Chan, D.-C., Hao, Y.-T., & Wu, S.-C. (2009a) <doi:10.1002/pds.1712>.
  Fincke, B. G., Snyder, K., Cantillon, C., Gaehde, S., Standring, P., Fiore, L., ... Gagnon, D.R. (2005) <doi:10.1002/pds.966>.
  Hovstadius, B., Astrand, B., & Petersson, G. (2009) <doi:10.1186/1472-6904-9-11>.
  Hovstadius, B., Astrand, B., & Petersson, G. (2010) <doi:10.1002/pds.1921>.
  Kennerfalk, A., Ruigómez, A., Wallander, M.-A., Wilhelmsen, L., & Johansson, S. (2002) <doi:10.1345/aph.1A226>.
  Masnoon, N., Shakib, S., Kalisch-Ellett, L., & Caughey, G. E. (2017) <doi:10.1186/s12877-017-0621-2>.
  Narayan, S. W., & Nishtala, P. S. (2015) <doi:10.1007/s40801-015-0020-y>.
  Nishtala, P. S., & Salahudeen, M. S. (2015) <doi:10.1159/000368191>.
  Park, H. Y., Ryu, H. N., Shim, M. K., Sohn, H. S., & Kwon, J. W. (2016) <doi:10.5414/cp202484>.
  Veehof, L., Stewart, R., Haaijer-Ruskamp, F., & Jong, B. M. (2000) <doi:10.1093/fampra/17.3.261>.
	"""
	
	cran = "polypharmacy" 

	version("1.0.0", md5="754a113797e4dbd91775251f5e60c4d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
