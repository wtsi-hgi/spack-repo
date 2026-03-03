# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RHicrep(RPackage):
    """R package to evaluate the reproducibility of Hi-C data (Genome Research 2017. doi: 10.1101/gr.220640.117.)"""

    homepage = "https://github.com/TaoYang-dev/hicrep"
    url = "https://github.com/MonkeyLB/hicrep/raw/master/hicrep_1.12.2.tar.gz"

    version("1.12.2", sha256="07a0369fb5e28dadc894720549c714710476ceb82c54842d8722393bd8145533")

    depends_on("r-stat", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-strawr", type=("build", "run"))
