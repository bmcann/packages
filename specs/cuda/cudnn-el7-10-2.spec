%global __os_install_post %{nil}

Name:           cudnn-10-2
Version:        7.6.5.32
Release:        2
Summary:        CUDA Deep Neural Network library

License:        NVIDIA Proprietary
Group:          Unspecified
URL:            https://developer.nvidia.com
Source0:        cudnn-10.2-linux-x64-v7.6.5.32.tgz

Vendor:         Nvidia
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
BuildArch:      x86_64
Requires:       cuda-license-10-2 >= 10.2.89
Prefix:         /usr/local/cuda-10.2
Prefix:         /usr/lib64/pkgconfig

%description
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library
of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

This RPM was packaged for CentOS 7 with libraries built against CUDA 10.2.

%prep
%setup -q -n cuda
%{__rm} -f lib64/libcudnn.so
%{__rm} -f lib64/libcudnn.so.7

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-10.2
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-10.2/lib64
%{__mkdir} -p %{buildroot}%{_prefix}/local/cuda-10.2/include
%{__install} -m 644 NVIDIA_SLA_cuDNN_Support.txt %{buildroot}%{_prefix}/local/cuda-10.2/
%{__install} -m 755 lib64/libcudnn.so.7.6.5 %{buildroot}%{_prefix}/local/cuda-10.2/lib64/
%{__install} -m 644 lib64/libcudnn_static.a %{buildroot}%{_prefix}/local/cuda-10.2/lib64/
%{__ln_s} -f libcudnn.so.7 %{buildroot}%{_prefix}/local/cuda-10.2/lib64/libcudnn.so
%{__ln_s} -f libcudnn.so.7.6.5 %{buildroot}%{_prefix}/local/cuda-10.2/lib64/libcudnn.so.7
%{__install} -m 644 include/cudnn.h %{buildroot}%{_prefix}/local/cuda-10.2/include/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/local/cuda-10.2/NVIDIA_SLA_cuDNN_Support.txt
%{_prefix}/local/cuda-10.2/lib64/libcudnn.so.7.6.5
%{_prefix}/local/cuda-10.2/lib64/libcudnn_static.a
%{_prefix}/local/cuda-10.2/lib64/libcudnn.so
%{_prefix}/local/cuda-10.2/lib64/libcudnn.so.7
%{_prefix}/local/cuda-10.2/include/cudnn.h

%changelog
* Fri Apr  8 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 7.6.5.32
- Make better use of RPM macros and add "__os_install_post" global setting to
  prevent binary stripping so that binary files are packaged without
  modification and thus have the same checksum as those in the original tarball

* Tue Apr  5 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 7.6.5.32
- Correct symlinks to libcudnn.so.7.6.5

* Tue Sep 22 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 7.6.5.32
- Package libcudnn for CentOS 7 and CUDA 10.2
