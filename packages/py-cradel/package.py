from spack.package import *


class PyCradel(PythonPackage):
    """Correct Read Counts and Analysis of Differently Expressed Regions"""

    homepage = "https://github.com/ReddyLab/CRADLE"
    url = "https://github.com/ReddyLab/CRADLE/archive/refs/tags/v0.30.1.tar.gz"
    git = "https://github.com/ReddyLab/CRADLE.git"

    license("MIT")

    version("0.30.1", sha256="d2e3d3eee3d5453dcc702e15b5511702198b4ccce7778a43e8ca76445f6353f5")
    version("0.30.0", sha256="b96990a91ef9d4534e2a167859e288beacd01a448b5fd9db420af6f3b5c3b244")
    version("0.29.0", sha256="349191ef9d648d682c0ea08a33cca9baea2095e485fdd82d4839befd5f0ff8da")
    version("0.28.0", sha256="19e649db09f4d371fe696e1f365fc7159958472ff1ece0323e0691447a125591")
    version("0.27.0", sha256="9f00ed21284d3c426d9f9b27db2dd011ae235f96774dafabd6789b7efb5fd86c")
    version("0.26.1", sha256="7a490c8074806bd8c43863a6ab9758bd74674ee47ae9e424ed56600f1f5cb556")
    version("0.26.0", sha256="eee3253069cda497304f2ce16d80fc52edcef2c0403ced8d216612b70257005b")
    version("0.25.1", sha256="40aa0beaaeea0af2a644597449e374c076bbcfdbcbb1e75aad722c97bc931671")
    version("0.25.0", sha256="a3732cd7a1f7bf4cb1a2146b7f2e8e12dc741be48fb5307103f94fafc442e89e")
    version("0.24.2", sha256="131192d8029e1f9af04b142713c006ec9bd42e3b26b8bd4d3675e3dbbae4e103")
    version("0.24.1", sha256="e3cca30e804851782440992dd158d57f6ec59509d899e8567f40c9ad4e22c6c2")
    version("0.24.0", sha256="da2762ab8aa48f1e7449755b6141253703ccab2b74bc644aead07cc7f84576ce")
    version("0.23.0", sha256="062140bba7763b5a152a277489d1b8bb0d6687f6ed5fc4bbc01d86fd59a3339d")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython@0.24.1:", type="build")
    depends_on("py-numpy@1.14.3:", type=("build", "run"))
    depends_on("py-py2bit@0.3.0:", type=("build", "run"))
    depends_on("py-pybigwig@0.3.11:", type=("build", "run"))
    depends_on("py-statsmodels@0.8.0:", type=("build", "run"))
    depends_on("py-scipy@1.0.1:", type=("build", "run"))
    depends_on("py-matplotlib@1.5.3:", type=("build", "run"))
    depends_on("py-h5py@2.6.0:", type=("build", "run"))
    depends_on("openblas", type=("build", "run"))  # ensure numpy's OpenBLAS backend is discoverable

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        for libdir in self.spec["openblas"].libs.directories:
            env.prepend_path("LD_LIBRARY_PATH", libdir)

    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        for libdir in self.spec["openblas"].libs.directories:
            env.prepend_path("LD_LIBRARY_PATH", libdir)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            cradle = Executable(join_path(self.spec.prefix.bin, "cradle"))
            cradle("--help")
