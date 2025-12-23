'use client';

import { useState } from 'react';
import api from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import { useRouter } from 'next/navigation';

export function AuthForm({ type }: { type: 'login' | 'register' }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const { login } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const endpoint = type === 'login' ? '/auth/login' : '/auth/register';
      const data = type === 'login' 
        ? { email, password }
        : { email, password, first_name: firstName, last_name: lastName };
      
      const response = await api.post(endpoint, data);
      login(response.data.access_token);
      router.push('/');
    } catch (error) {
      alert('Ошибка авторизации');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-md mx-auto mt-20">
      <h1 className="text-3xl font-bold">
        {type === 'login' ? 'Вход' : 'Регистрация'}
      </h1>
      
      {type === 'register' && (
        <>
          <input
            type="text"
            placeholder="Имя"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            className="w-full p-3 border rounded"
          />
          <input
            type="text"
            placeholder="Фамилия"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            className="w-full p-3 border rounded"
          />
        </>
      )}
      
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="w-full p-3 border rounded"
        required
      />
      
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full p-3 border rounded"
        required
      />
      
      <button
        type="submit"
        className="w-full bg-red-600 text-white p-3 rounded hover:bg-red-700"
      >
        {type === 'login' ? 'Войти' : 'Зарегистрироваться'}
      </button>
    </form>
  );
}