# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libcuml(CMakePackage):
    """cuML is a suite of libraries that implement machine
    learning algorithms and mathematical primitives functions
    that share compatible APIs with other RAPIDS projects."""

    homepage = "https://rapids.ai"
    url = "https://github.com/rapidsai/cuml/archive/v0.15.0.tar.gz"

    version("24.06.00", sha256="f45e4656ce77e672b2f184b460b23b1ac0c71503e328f3028707f38feb4c8e55")
    version("24.04.00", sha256="ddac91479aa6dff80c3a966932d5bc39de461d89d3014c7ac09569711c0c9b49")
    version("24.02.00", sha256="5ae031503756313ff0398c9d67c0a24825db0fa103605dca30dd9ccb5a0b30ef")
    version("23.12.00", sha256="ffc92c8b943fbf30d1f55413e204fbbc1c98db2b4310ad0421db98e087d97b34")
    version("23.10.00", sha256="bd5060033efeb47667a1616d1479838325451db5f473324191e0328302ab75c7")
    version("23.08.00", sha256="a17b426ee0601821b891921812ea8b0c78926033d0d73da304c9ce302060614d")
    version("23.06.00", sha256="4f5269177b5cdb4f4821529eb0ec03057acc80299290e7a9e8dc56ed4ae1c3c2")
    version("23.04.00", sha256="c8036ad8d43ff72b5e5fef8048514562b2bd553f4b2e7b31be272f21298b3b6b")

    depends_on("cmake", type="build")
    depends_on("zlib-api")
    depends_on("libcudf@0.8:")
    depends_on("cuda@9.2:")
    depends_on("blas")
    # depends_on("nccl")
    depends_on("treelite")
    depends_on("googletest")
    # depends_on("libcumlprims")
    depends_on("mpi")
    depends_on("ucx")
    depends_on("doxygen")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        args = []

        args.append("-DBUILD_CUML_C_LIBRARY=ON")
        args.append("-DNVTX=OFF")
        args.append("-DSINGLEGPU=ON")

        return args
