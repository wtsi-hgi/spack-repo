# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerarma(RPackage):
	"""Periodic Time Series Analysis

	Identification, model fitting and estimation for time series with periodic structure.
    Additionally, procedures for simulation of periodic processes
    and real data sets are included.
    Hurd, H. L., Miamee, A. G. (2007) <doi:10.1002/9780470182833>
    Box, G. E. P., Jenkins, G. M., Reinsel, G. (1994)  <doi:10.1111/jtsa.12194>
    Brockwell, P. J., Davis, R. A. (1991, ISBN:978-1-4419-0319-8) 
    Bretz, F., Hothorn, T., Westfall, P. (2010, ISBN: 9780429139543) 
    Westfall, P. H., Young, S. S. (1993, ISBN:978-0-471-55761-6)
    Bloomfield, P., Hurd, H. L.,Lund, R. (1994) 
    <doi:10.1111/j.1467-9892.1994.tb00181.x>
    Dehay, D., Hurd, H. L. (1994, ISBN:0-7803-1023-3)
    Vecchia, A. (1985) <doi:10.1080/00401706.1985.10488076>
    Vecchia, A. (1985) <doi:10.1111/j.1752-1688.1985.tb00167.x>
    Jones, R., Brelsford, W. (1967) <doi:10.1093/biomet/54.3-4.403>
    Makagon, A. (1999)
    <https://www.math.uni.wroc.pl/~pms/files/19.2/Article/19.2.5.pdf>
    Sakai, H. (1989) <doi:10.1111/j.1467-9892.1991.tb00069.x>
    Gladyshev, E. G. (1961) 
    <https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=dan&paperid=24851>
    Ansley (1979) <doi:10.1093/biomet/66.1.59>
    Hurd, H. L., Gerr, N. L. (1991) <doi:10.1111/j.1467-9892.1991.tb00088.x>.
	"""
	
	cran = "perARMA" 

	version("1.7", md5="e044d6e933c1059876aac37c50c62014")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
