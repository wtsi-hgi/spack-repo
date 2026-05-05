# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHdf5plugin(PythonPackage):
    """HDF5 Plugins for Windows, MacOS, and Linux"""

    homepage = "https://github.com/silx-kit/hdf5plugin"
    pypi = "hdf5plugin/hdf5plugin-6.0.0.tar.gz"

    version("1.0.0", sha256="9a3d6315f7da7a5791c3a1c47daaf6c4bc5216ad661f73f0609892b130ded9af", expand=False, url="https://files.pythonhosted.org/packages/f6/ab/5cc16dfba63df7b4409a7e637e73bf92c7ed528f8084602bad95ac047814/hdf5plugin-1.0.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="c7e482eb420b4eb19805322efe5ee287e0474b80ed17235dc6fe90d3b27d2b12", expand=False, url="https://files.pythonhosted.org/packages/a4/00/38f5414ae524a97a3c180a04ad0f11db2177de64491e3d79d79018723031/hdf5plugin-1.0.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="58c402fa537504b69eb3820b9ee8eb6c640a494a1bb4b637e723c74670ff5475", expand=False, url="https://files.pythonhosted.org/packages/b4/57/db41c06d174fea414dca362da26d0f9e9220918d646f68f65e3163541f28/hdf5plugin-1.1.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="85994a6a6cc49c48845f69e2f9a4551a6769d56cb2f7364ffcd2bbd261833fda", expand=False, url="https://files.pythonhosted.org/packages/0b/ba/5aca116687712ab2178b61d5dece78ee29f268ca1f258ea9bd888410f8f9/hdf5plugin-1.2.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="a973814e51cea9e788c7ebf761bf81d74b74ec109b4b6e228d3b01aaf56d09e6", expand=False, url="https://files.pythonhosted.org/packages/40/2e/23dc5c9713f2f58235c4425120822e6c60d8ef1ca83137ae93c1c49d2440/hdf5plugin-1.3.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="b26f064f3308b1543b8ae45b0b666c8b8ede31bdd32a0a7638085b9053db21b7", expand=False, url="https://files.pythonhosted.org/packages/00/0c/b365f3632327f4c0a5fdcfde724e40951b53e64e39326f99732d71d23149/hdf5plugin-1.4.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="bbff4ec5b09e4797e76277c9b1a0bc7b2c7c6478d2ce4df7760ab28a2d167a84", expand=False, url="https://files.pythonhosted.org/packages/cf/a9/3616bc97c566d0d375dfcf362cbd5dcedebfe55cec1fb86585d1aa8bd463/hdf5plugin-1.4.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="3b2cb962b122ef08543fdcd69237d3d175b60302d1063bdca8611cbf13e71bf7", expand=False, url="https://files.pythonhosted.org/packages/87/04/a19e98a1dc749a3725107888604d6f5fb03ae46a3fca300749c0a85b3b3e/hdf5plugin-2.0.0-py2.py3-none-manylinux1_x86_64.whl")
    version("2.0.0b0", sha256="8180812c71f5f66cbe96a3106a8fa1350de29d899d11456e8ad3a138ef3513b8", expand=False, url="https://files.pythonhosted.org/packages/30/3f/faf8255401334d667cfaf782a2d06ba488ee3ef8b93c764bb60a02dfd964/hdf5plugin-2.0.0b0-py2.py3-none-manylinux1_x86_64.whl")
    version("2.1.0", sha256="3d8da71344359d5bd1cc230d70e8aca05bbfaddca801c8d87f5b54bd4fc30b41", expand=False, url="https://files.pythonhosted.org/packages/50/f7/f15f90f8450ce63aa9b3b6821f3a919d353a6242bf349102dda16be0a70a/hdf5plugin-2.1.0-py2.py3-none-manylinux1_x86_64.whl")
    version("2.1.1", sha256="de41c488395d0a7fdf96e5c7cfa5c01a8a5dd1fef2476f5b8d800b41eccc2be0", expand=False, url="https://files.pythonhosted.org/packages/83/89/7a8f03277e2ab5738367dcfb34cc22aaa707f7fb5162a00431cdcc9df126/hdf5plugin-2.1.1-py2.py3-none-manylinux1_x86_64.whl")
    version("2.1.2", sha256="0ae84eb304613a7d7d595842535ff01a3341250116fd3a1714526f7dd9dca624", expand=False, url="https://files.pythonhosted.org/packages/a7/12/3b9f57a40dc81edd7eeb01850466ba511b1fdfd3e34ef9d666f79c42f50c/hdf5plugin-2.1.2-py2.py3-none-manylinux1_x86_64.whl")
    version("2.2.0", sha256="b25b3fb5391351a1c27a56fa9026f2b00b5992367b2b94a8eb489b8854c7f0fb", expand=False, url="https://files.pythonhosted.org/packages/d9/b6/77d659813d4167605546dfd2bd0f20a9f85208d16f5effcc3f8b8c6c89b9/hdf5plugin-2.2.0-py2.py3-none-manylinux1_x86_64.whl")
    version("2.3.0", sha256="39d71d1f3a412c5461b93285eeb28c6429a19f9e199669c57684b60f38fd968b", expand=False, url="https://files.pythonhosted.org/packages/1b/2a/c9f9a0f4bfc1a2afc1202bf03936baace6906f925ebc40661d1f3393453a/hdf5plugin-2.3.0-py2.py3-none-manylinux1_x86_64.whl")
    version("2.3.1", sha256="4714d0f12136ea3312689d14b2a0151def527acc14dd7aa1c90a622641249b1e", expand=False, url="https://files.pythonhosted.org/packages/7c/e9/fbe1ab3e69aaece145ecb05ec2cef7e5fa45859e4054fd96581339fe8faa/hdf5plugin-2.3.1-py2.py3-none-manylinux1_x86_64.whl")
    version("2.3.2", sha256="d66d8327ca87aba9f4e8832dff87ecb5924991719b1fcbdef653fdf40e38997a", expand=False, url="https://files.pythonhosted.org/packages/7a/e9/fafd6b0ea54ae9422e78f87ed0a88e78abc6f6d78de2923b76789f45aa2e/hdf5plugin-2.3.2-py2.py3-none-manylinux1_x86_64.whl")
    version("3.1.0", sha256="0fc396ae6865e13da67ceb9d72ffc93a079e097ea8a4810f6d1bdb38a9a3b148", expand=False, url="https://files.pythonhosted.org/packages/fb/2a/55d91beb3bf429aacb748aaaa721cacb77c81d0a769986d82653bb13fea5/hdf5plugin-3.1.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
    version("3.1.1", sha256="868a843653774d22e80477ffe145ba55ef853cebe018d97934ce0faf28bb1574", expand=False, url="https://files.pythonhosted.org/packages/28/cc/237c31ba5c9db4b635744f937e87d3326ded44ac2434aa4773e4e897f033/hdf5plugin-3.1.1-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
    version("3.2.0", sha256="ed2f22c4aa6d8cea747fe6335bf6531d0844a628f32569dd40849b819aaed785", expand=False, url="https://files.pythonhosted.org/packages/7e/6f/249ed3f8226c341385fc7b878042cd91ea823a48d64259e7346c8fc09b09/hdf5plugin-3.2.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
    version("3.3.0", sha256="3882c2cd336d95eb24602c2c360c467e8617d80976e59482afd72eb0fe0fdafc", expand=False, url="https://files.pythonhosted.org/packages/a2/84/fd83a2418f08696802082238b5175098214df7f461e71f6265aa292b374c/hdf5plugin-3.3.0-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
    version("3.3.1", sha256="b06b46c448af878be46d4cf480b03b1d576b7bf04d3d8f4cbf40f8fd75086fb4", expand=False, url="https://files.pythonhosted.org/packages/22/55/8f35321ff689a26cd8b99c4cae3908decd007f7553e651f6141ef9853465/hdf5plugin-3.3.1-py3-none-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
    version("4.0.0", sha256="58da2df01698be96dc4db6ec1639854b3425aae14bb8a0d6d9e1f9dbbb955c5e")
    version("4.0.1", sha256="b185fea987f582e3a51e7994cc07415664ac8be54dbad863d9f65a4fb5bd635c")
    version("4.1.0", sha256="d59afda87eaba5810d34b739d7b167d37a4e998144c1b325ea818d7afb483964")
    version("4.1.1", sha256="96a989679f1f38251e0dcae363180d382ba402f6c89aab73ca351a391ac23b36")
    version("4.1.2", sha256="fa954e93061a1376380734cd05e2f1d68baab53101d23bfb0ce6e4ffc6f65be0")
    version("4.1.3", sha256="40838a6f39a84d2b7f3b9c3b88a7a89d0df99851756f5481ea11a05b07f60622")
    version("4.2.0", sha256="500c3de00fb80b3a588808776e89a90e8f2fc5353f0b5e921750c93030ed2d36")
    version("4.3.0", sha256="0face8ee85817f168ab97cd72bd83dfd2803adbe7fc4881c5edf5b064ecb3684")
    version("4.4.0", sha256="4142f54170843782eda7456b8f47d15910879ceb2608025aebf9464b7163913a")
    version("4.4.0b0", sha256="1240f2f26752d92c89b845a36f7fd98c391d572068fb22a75b1e6441bead205c")
    version("5.0.0", sha256="3bcc5c4f523953fe020a220c7b1b307c62066e39fdbdcd904fa2268db80e9dbb")
    version("5.1.0", sha256="cf78f1426b5868128b9ec6c498b70d6734e1dc8007a8ed1e7282954ab421b3fa")
    version("6.0.0", sha256="847ed9e96b451367a110f0ba64a3b260d38d64bbf3f25751858d3b56e094cfe0")

    depends_on("py-setuptools@77:", type=("build"))
    depends_on("py-py-cpuinfo", type=("build"))
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-h5py@3:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        python("-c", "import hdf5plugin")
