# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGa(RPackage):
    """Flexible general-purpose toolbox implementing genetic algorithms (GAs) for stochastic optimisation. Binary, real-valued, and permutation representations are available to optimize a fitness function, i.e. a function provided by users depending on their objective function. Several genetic operators are available and can be combined to explore the best settings for the current task. Furthermore, users can define new genetic operators and easily evaluate their performances. Local search using general-purpose optimisation algorithms can be applied stochastically to exploit interesting regions. GAs can be run sequentially or in parallel, using an explicit master-slave parallelisation or a coarse-grain islands approach."""

    homepage = "https://luca-scr.github.io/GA/"
    cran = "GA"

    version("3.2.3", sha256="eb3a11798d42a7f105834363f571f7ca435728a5a6a324c703d7d2f9cbc90b60")
    version("3.2.2", sha256="6245c634a11b8414bde7ed326b8c615512645489b19969619484c865e900bf8c")
    version("3.2.1", sha256="b494d970b9a2876fdb805d2ba0ac7d8a2cfd875b4e432d1c532cdb1b50eb562d")
    version("3.2", sha256="c7a001b9354a3ea6280362ddb2d1e5dc7ede2bc324fd9564a58c42ccfe6a75ec")
    version("3.1.1", sha256="bfd5dc048abe9d9426b560a075e2c386f356e9811277488f8145516f1a548800")
    version("3.1", sha256="9a973c035036872cead0f79e16dcc9eb94e96fce541efa61f5b483ca13b5dee4")
    version("3.0.2", sha256="9d9bf60371e5da08ce923d0584f7677864659fcb759b2d43b634eeeea35def4a")
    version("3.0.1", sha256="719eb6e5215c28e5a7e9bf7702d8f255f079d191237533f2fd006aa697923fd2")
    version("3.0", sha256="0f6adba4c13546ff7794ecedfb51e34b8540527783c17cab126adcc3a0d5d929")
    version("2.2", sha256="773acf41f17fcdabd53b7aa447d78f6d4a44370e6378e05a30b1defdb90468de")
    version("2.1", sha256="8479664b87c82fd08eb36637b6e138de2472c7c1cf7862ff4cac6cd5a6894d19")
    version("2.0", sha256="5f90464e6dd0b6c2cd9f0ca15b6994c14ad6e2238737016c4395eca597ec9d2d")
    version("1.1", sha256="372a74c291be12ca73ac540a7ab41120a4e66306a017155e0f5c15f5c8bdbe88")
    version("1.0", sha256="5add612106d0d49d0193c63fcee6fe5efc7130f8b60f839ad3d76c633fde953d")

    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
