# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDatacache(PythonPackage):
    """Helpers for transparently downloading datasets"""

    homepage = "https://github.com/openvax/datacache"
    pypi = "datacache/datacache-1.4.1-py3-none-any.whl"

    version("0.1", sha256="b5be46fb7d10dbd6527fc2c693949afa7b86cc3bca5a49feb6789adb13f9b70a")
    version("0.2", sha256="1266f881bb3296127e19738288fd173483f7be7aa72994ea4459bf4de68734f1")
    version("0.3", sha256="d3ce77294465d2f466041c2945f5dccdb3ac4980d519ec897067cab4e898b911")
    version("0.3.1", sha256="51eff5176086340c1357540ef7078a81e992a2f931aee09c0de6782fe2f3a3b2")
    version("0.3.2", sha256="b1c0ca19cfdb90ba7de7937d130b2c0db010851edfa62f92833260cd17b31a91")
    version("0.3.3", sha256="c5132bb3d343a9c5d9be390295aa26d61ff9f14bd3245e8718da8cdbdba4fc34")
    version("0.3.4", sha256="f7014df1439ed1b9e0babc31bb4a2802d63a2097234b564358b4e759d7e8fae3")
    version("0.3.5", sha256="bb1cbb32531883de02d645c3d2814deee15ea719f2d52385fb8461b0c0c2e858")
    version("0.3.6", sha256="38ac2c3125a06044a2e5c490a3a298f1b6e1e9da4addb5f148350688468beb6b")
    version("0.3.7", sha256="a7af0ea4454bcd74a8fd5f7191d3f117c5f1b7d4418c03022d350573b878f251")
    version("0.3.8", sha256="4b5cbcd7a9b316771fc444f0b6b00f74e4ee6c274523224cc67f16fa080ee4b9")
    version("0.4.0", sha256="1d187582402d7b1398cf529655c6a7d82f35db73e8cf51fed255c5db7977b0a2")
    version("0.4.1", sha256="c85ec29d564f904d4fc80e9a741dc5fe7287d5148a1d6a0d9b4de5d9ef9334b3")
    version("0.4.10", sha256="811fd3a4aa0cc95d7f8a913e98f744901661f21500eae328a2a1d1657f4c61b9")
    version("0.4.11", sha256="4669a645d552a10b65e923d61df4cdb7e83d882c678c55b89ff315068e466b52")
    version("0.4.12", sha256="17d7ac0e033eb960447b45833ff9d2e0862b46f16c29412212f6a2c4bbeec61f")
    version("0.4.13", sha256="9440ac416fe3bc4e4b3d8a81aa6d8a7ae56475423ac59785d11ae9a152ad7236")
    version("0.4.14", sha256="ad0e247ab3d35a679993edb166b1ad22795369e2f77c01b13883c484b6b24661")
    version("0.4.15", sha256="cdfa700461d1b0d8ee6c7aba1de6d4c82006e48c302e1cc13dacd5e42fe90d67")
    version("0.4.16", sha256="392f5eaf0f098194df4a07215ccc2d2542ef8df8fc1990cffcc4663ee3a29f85")
    version("0.4.17", sha256="7961482ec931e77458ec3954e5840a29a320787625e849332f9f19e9d9b302a6")
    version("0.4.19", sha256="3f39c8d4fd3e69d712e90e6068622b57d5aa43e25fa4479d40d0150cb47af855")
    version("0.4.2", sha256="793234b92a5689f3f4e355c994440b4db883285ca55a9dae833e7d6a5c16ca67")
    version("0.4.20", sha256="ad644a605dd1c1f054f7f68d67ee5102ed0461cf612870600f59e7020a254044")
    version("0.4.3", sha256="c7ca10972e3fc570ff89e1b82ca799b6362c42d0c04c7f8cba3e9efc3d224363")
    version("0.4.4", sha256="0ed804b878bcd54fe616e4f9e54839a559457da029d4c2b58330c73f7e6e9f8c")
    version("0.4.5", sha256="48e08d1ec68418a07a8ff989f4f66c68d0174573ba54f9f2dea4e7c8f0391d28")
    version("0.4.6", sha256="a927df2c597cb3f087e792feaca6a0c6324df59ae1ab38732bacfaa7a1947688")
    version("0.4.8", sha256="dc29f0a8c087b5dd8daf17664cbfefa7c24c702fe163548c74c560fcfc7a173c")
    version("0.4.9", sha256="681d44187e41426ac99e2d5a48dfb181e47c796464bc20216a256af0f58ae398")
    version("0.5.2", sha256="ce3a46144345d3152a3c91f2b04d6e63d0636804238a9aef4c844d27ac3c5f77")
    version("0.5.3", sha256="398cbe024de04956ffd3312f76344c1ba588f2f9811f57ff4203dd261e937707")
    version("0.5.4", sha256="1a24cc40c6e88990304354a7705aa103ce61a449239062b83cfab9f40933bb8c")
    version("0.5.5", sha256="29bce433db1f379e1439ca640b59a8ebce617cf500667ebb48d70c1dc2c40cc5")
    version("1.0.0", sha256="a936a71dfb6ab3d396080eafff8c934dc363fcaac8c576647beafe96e26c068e")
    version("1.1.0", sha256="4d22c9d5e045739519a25b5e5ed845df76bdb29ce081a00dcda00b5c8fcb3fdf")
    version("1.1.3", sha256="9e477f30f809e1464f79d7227bf64ee7dad25b32adf804f6ea89203bc27cb811")
    version("1.1.4", sha256="624a285dcf07778668a4c85e6f03c4777f999a512651dd218249d0f2b4f9c8ba")
    version("1.1.5", sha256="b2ca31b2b9d3803a49645ab4f5b30fdd0820e833a81a6952b4ec3a68c8ee24a7")
    version("1.2.0", sha256="f7b4c903baf046b56d6a8b060d1b856c066399becbfd51bb1ca0e72d4ba756ff")
    version("1.2.1", sha256="ed24c419ed9791ef0f0375ca5552b2300922235ee9ffa81d200f002c6f7d7955")
    version("1.3.0", sha256="1ec99f176ed8c93290a8556ec126baed38ffa2d4d7e1c91706ae7acb83c9d717", expand=False, url="https://files.pythonhosted.org/packages/b6/4c/30ab7b4f8d2737e3682cf5c3f552ba6ad4aacd0e43366270eebf766bdb45/datacache-1.3.0-py3-none-any.whl")
    version("1.4.0", sha256="771b4cb11ad2eff1f5c95cfb24ac8f7df474f8368fe049533652480d3ff612d9", expand=False, url="https://files.pythonhosted.org/packages/86/34/606bbcfa507ddc0209f75865e3684a61853925f99b9ffd164d78e2b86271/datacache-1.4.0-py3-none-any.whl")
    version("1.4.1", sha256="a334747a2b849d7e4aa09aff3bc338ee10a97f02e5fe0237b6bb9254b4779635", expand=False, url="https://files.pythonhosted.org/packages/63/bf/585fd1522561df26ae44caf40c827cb2f0ec3de5b2bb00d26117ad6b7663/datacache-1.4.1-py3-none-any.whl")

    depends_on("py-setuptools", type="build")
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-appdirs", type=("build", "run"))
    depends_on("py-progressbar33", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-typechecks", type=("build", "run"))
    depends_on("py-mock", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import datacache")

# {'pandas>=0.15.2': ['1.3.0', '1.4.0', '1.4.1'], 'appdirs>=1.4.0': ['1.3.0', '1.4.0', '1.4.1'], 'progressbar33>=2.4': ['1.3.0', '1.4.0', '1.4.1'], 'requests>=2.5.1': ['1.3.0', '1.4.0', '1.4.1'], 'typechecks>=0.0.2': ['1.3.0', '1.4.0', '1.4.1'], 'mock': ['1.3.0', '1.4.0', '1.4.1']}
