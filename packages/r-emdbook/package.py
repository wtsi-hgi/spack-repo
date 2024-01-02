# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdbook(RPackage):
    """Auxiliary functions and data sets for "Ecological Models and Data", a book presenting maximum likelihood estimation and related topics for ecologists (ISBN 978-0-691-12522-0)."""

    #url = "https://cran.r-project.org/src/contrib/emdbook_1.3.13.tar.gz"
    cran = "emdbook"

    version("1.3.13", sha256="26044b7ea1b42304b4dfde48afa94dd487acf979da4db2bf670ba41222083c19")
    version("1.3.12", sha256="0646caf9e15aaa61ff917a4b5fdf82c06ac17ef221a61dec3fbb554e7bff4353")
    version("1.3.11", sha256="f848d4c0a2da50dc8a5af76429d8f9d4960dee3fad1e98f7b507bdfd9b2ca128")
    version("1.3.10", sha256="bbc25496daea534e9919bc84a98e7f0051f72298a2d9fe457b3b559c4d670021")
    version("1.3.9", sha256="c978c82e8baaade81c9152f3c2b6225e5ae0576e28fb3c9ecefb1285b86fab27")
    version("1.3.8", sha256="523a772552c3d17e507d3858f7dcce3be69d9bba2e3508c3e38873c7d4bd1583")
    version("1.3.7", sha256="41892376f9cb4ac2c2044211c9548ad17df9069de5c945e00ab09ce4664d928c")
    version("1.3.6", sha256="38708f4494035aeebe53618e55c374672963973d385e588975362b7ec11efec6")
    version("1.3.4", sha256="4df89b4f083cd0dd80baeee1f6a6535246c36576192ba9ce610f6f73798828a6")
    version("1.3.2.1", sha256="60892d18a27e5a718ff0e96ac0733c12060e341c75854c973dcfa9ae576d241b")
    version("1.3.2", sha256="fb2efa1c912e878c6ab0aa9bc403ac11979761b3835fbae60c26aeccfd81d060")
    version("1.3.1", sha256="31b753a7d1f8481df9cc9779d89742dc0ce60cedb92537fdb53e58c83ba5c195")
    version("1.3", sha256="c152e07d9d73c2260969ba261155bfaddcb36a099572e0fa03a5616d9e243303")
    version("1.2.2.2", sha256="e05538d7ec99cc8c9ec467fbdf8256a9e5b6a9b0c2ae9d9155b2f453ad0e7a67")
    version("1.2.2.1", sha256="319e50dac74b522519c333d98cbdd6f665c5fc3dfc8916fbfbc0a51ea644fa08")
    version("1.2.1", sha256="7dc1a81fa486ca8ecf3905bacb7ecdb3d2f0cfc52e1537d2f7579667f143460b")
    version("1.2", sha256="5928cb199236db5338bedcc19111fb0297d7f1932951768e92fb222017d08ca2")
    version("1.1.1.1", sha256="4967d2a81f6c9f53e8bd8815523c7847b3317fa881c8f9ba72fa9373d5cee3a7")
    version("1.1.1", sha256="b400fce4028c56e8c022762294e0a9dc2d3a67c8ac457ebab0acef36a4c7314c")
    version("1.0.9", sha256="35efe3faa03fb88f18e4089da82b87518e9f05208b3bbe576b61bfb79ba926c7")
    version("1.0.8.1", sha256="554193a64149090dc4b2e67743676161ac27507fdaa88bc04f07fb20b0f9e5da")
    version("1.0.6", sha256="d5e3893e18cf826e680f8890baed2fd0f08d9d375498c2fcffe54044c0f48127")
    version("1.0.5", sha256="7a471fd6b784994e4b778c6f74d9bcf26f3a621164668c72f433c69d4e86ae8d")

    depends_on("r-mass", type=('build', 'run'))
    depends_on("r-lattice", type=('build', 'run'))
    depends_on("r-plyr", type=('build', 'run'))
    depends_on("r-coda", type=('build', 'run'))
    depends_on("r-bbmle", type=('build', 'run'))
