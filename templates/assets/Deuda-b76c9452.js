import{j as s,q as l,r as c,s as d}from"./index-57f3d5cd.js";import{T as o}from"./TitleCard-3b48e0e6.js";import{u as x,T as h}from"./TrashIcon-d6d6b5d5.js";import{u as j}from"./Layout-b7e568d0.js";const m=()=>s.jsx("div",{className:"inline-block float-right",children:s.jsx("button",{className:"btn px-6 btn-sm normal-case btn-primary",onClick:()=>{},children:"Add New"})});function u(){const{isLoading:e,isError:t,data:a,error:n}=x(["deudas"],l);return e?s.jsx("span",{children:"Loading..."}):t?s.jsxs("span",{children:["Error: ",n.message]}):s.jsx(s.Fragment,{children:s.jsx(o,{title:"Deudas",topMargin:"mt-2",TopSideButtons:s.jsx(m,{}),children:s.jsx("div",{className:"overflow-x-auto w-full",children:s.jsxs("table",{className:"table table-zebra w-full",children:[s.jsx("thead",{children:s.jsxs("tr",{className:"bg-base-200 borde",children:[s.jsx("th",{children:"User"}),s.jsx("th",{children:"Mes"}),s.jsx("th",{children:"Estado"}),s.jsx("th",{})]})}),s.jsx("tbody",{children:a.map((r,i)=>s.jsxs("tr",{children:[s.jsx("td",{children:s.jsx("div",{className:"flex items-center space-x-3",children:s.jsx("div",{className:"font-bold",children:r.user})})}),s.jsx("td",{children:r.mes}),s.jsx("td",{children:r.estado_reserva}),s.jsx("td",{children:s.jsx("button",{className:"btn btn-square btn-ghost",onClick:()=>{},children:s.jsx(h,{className:"w-5"})})})]},i))})]})})})})}function N(){const e=j();return c.useEffect(()=>{e(d({title:"Deuda"}))}),s.jsx(u,{})}export{N as default};